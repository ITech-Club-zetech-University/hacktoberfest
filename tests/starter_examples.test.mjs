import assert from "node:assert/strict";
import { createRequire } from "node:module";
import { mkdtemp, writeFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";
import { generate, main } from "../examples/gemma/hosted.mjs";

const require = createRequire(new URL("../examples/gemma/package.json", import.meta.url));
const { GoogleGenAI } = require("@google/genai");

function client(requests, response, status = 200) {
  return new GoogleGenAI({
    apiKey: "offline-test-not-a-real-key",
    httpOptions: {
      retryOptions: { attempts: 1 },
      fetch: async (url, init) => {
        requests.push({ url: String(url), body: JSON.parse(init.body) });
        return new Response(JSON.stringify(response), {
          status,
          headers: { "Content-Type": "application/json" },
        });
      },
    },
  });
}

test("real SDK serializes a text request with the documented Gemma model", async () => {
  const requests = [];
  const ai = client(requests, { candidates: [{ content: { parts: [{ text: " Model text " }] } }] });
  assert.equal(await generate(ai), "Model text");
  assert.equal(requests.length, 1);
  assert.match(requests[0].url, /gemma-4-26b-a4b-it:generateContent/);
  assert.equal(requests[0].body.contents[0].role, "user");
});

test("real SDK serializes permitted inline image bytes", async () => {
  const directory = await mkdtemp(join(tmpdir(), "hack-day-image-"));
  try {
    const image = join(directory, "sample.png");
    await writeFile(image, Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]));
    const requests = [];
    const ai = client(requests, { candidates: [{ content: { parts: [{ text: "Image text" }] } }] });
    assert.equal(await generate(ai, image), "Image text");
    const imagePart = requests[0].body.contents[0].parts[1].inlineData;
    assert.equal(imagePart.mimeType, "image/png");
    assert.equal(imagePart.data, "iVBORw0KGgo=");
  } finally {
    await rm(directory, { recursive: true });
  }
});

test("empty output is not a successful smoke test", async () => {
  await assert.rejects(generate(client([], {})), /No text returned/);
});

test("API quota error propagates rather than returning success", async () => {
  const ai = client([], { error: { code: 429, message: "offline quota test" } }, 429);
  await assert.rejects(generate(ai), /429/);
});

test("unsupported, missing, empty and oversized image inputs fail before inference", async () => {
  const directory = await mkdtemp(join(tmpdir(), "hack-day-invalid-"));
  try {
    const requests = [];
    for (const [name, data] of [["bad.txt", "not-image"], ["empty.png", ""], ["big.png", Buffer.alloc(5 * 1024 * 1024 + 1)]]) {
      const image = join(directory, name);
      await writeFile(image, data);
      await assert.rejects(generate(client(requests, {}), image));
    }
    await assert.rejects(generate(client(requests, {}), join(directory, "missing.png")), /ENOENT/);
    assert.equal(requests.length, 0);
  } finally {
    await rm(directory, { recursive: true });
  }
});

test("placeholder credentials produce a nonzero exit without inference", async () => {
  const previous = process.env.GEMINI_API_KEY;
  process.env.GEMINI_API_KEY = "replace_with_your_api_key";
  try {
    assert.equal(await main(), 1);
  } finally {
    if (previous === undefined) delete process.env.GEMINI_API_KEY;
    else process.env.GEMINI_API_KEY = previous;
  }
});

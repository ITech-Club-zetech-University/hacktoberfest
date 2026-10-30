import { readFile } from "node:fs/promises";
import { extname } from "node:path";
import { pathToFileURL } from "node:url";
import { GoogleGenAI } from "@google/genai";

export async function generate(client, imagePath) {
  const parts = [{ text: imagePath
    ? "Describe this image. Say what is uncertain."
    : "Explain open-source software in one sentence." }];
  if (imagePath) {
    const mimeType = { ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png" }[extname(imagePath).toLowerCase()];
    if (!mimeType) throw new Error("Use a JPEG or PNG image.");
    const data = await readFile(imagePath);
    if (data.length === 0 || data.length > 5 * 1024 * 1024) {
      throw new Error("Use a non-empty image no larger than 5 MiB (this example's limit).");
    }
    parts.push({ inlineData: { mimeType, data: data.toString("base64") } });
  }
  const response = await client.models.generateContent({
    model: "gemma-4-26b-a4b-it",
    contents: [{ role: "user", parts }],
  });
  if (typeof response.text !== "string" || !response.text.trim()) {
    throw new Error("No text returned. Check response safety/finish information before retrying.");
  }
  return response.text.trim();
}

export async function main() {
  const apiKey = process.env.GEMINI_API_KEY?.trim();
  if (!apiKey || apiKey === "replace_with_your_api_key") {
    console.error("ERROR: Set GEMINI_API_KEY in your environment or private .env.");
    return 1;
  }
  try {
    const client = new GoogleGenAI({ apiKey, httpOptions: { timeout: 60000 } });
    console.log(await generate(client, process.argv[2]));
    return 0;
  } catch (error) {
    if (error instanceof Error && "status" in error) {
      console.error(`ERROR: Gemma API status ${error.status}. Check access, model, quota and billing.`);
    } else {
      console.error("ERROR:", error instanceof Error ? error.message : String(error));
    }
    return 1;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  process.exitCode = await main();
}

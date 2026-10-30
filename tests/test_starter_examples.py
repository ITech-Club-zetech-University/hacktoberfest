"""Offline example checks; hosted SDK tests use a mock HTTP transport, never an API key."""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error


ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples" / "gemma"


def load_example(name):
    spec = importlib.util.spec_from_file_location(name, EXAMPLES / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestLocalGemmaExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = load_example("ollama")

    def test_completed_nonempty_response_and_request_shape(self):
        result = io.BytesIO(b'{"response": " Local text ", "done": true}')
        with patch("urllib.request.urlopen", return_value=result) as open_url:
            self.assertEqual(self.example.generate("hello"), "Local text")
        request = open_url.call_args.args[0]
        self.assertEqual(request.full_url, "http://localhost:11434/api/generate")
        self.assertEqual(json.loads(request.data), {
            "model": "gemma4:e2b", "prompt": "hello", "stream": False,
        })
        self.assertEqual(open_url.call_args.kwargs["timeout"], 120)

    def test_missing_model_has_pull_instruction(self):
        error = urllib.error.HTTPError("http://localhost:11434", 404, "missing", {}, None)
        with patch("urllib.request.urlopen", side_effect=error):
            with self.assertRaisesRegex(RuntimeError, "ollama pull gemma4:e2b"):
                self.example.generate("hello")

    def test_stopped_daemon_and_timeout_have_start_instruction(self):
        for error in (urllib.error.URLError("refused"), TimeoutError()):
            with self.subTest(error=type(error).__name__):
                with patch("urllib.request.urlopen", side_effect=error):
                    with self.assertRaisesRegex(RuntimeError, "ollama serve"):
                        self.example.generate("hello")

    def test_other_http_failure_is_explicit(self):
        error = urllib.error.HTTPError("http://localhost:11434", 500, "failed", {}, None)
        with patch("urllib.request.urlopen", side_effect=error):
            with self.assertRaisesRegex(RuntimeError, "HTTP 500"):
                self.example.generate("hello")

    def test_invalid_empty_error_and_incomplete_responses_fail(self):
        for data in (
            b"not-json", b"[]", b'{"error":"load failed"}',
            b'{"response":"", "done":true}', b'{"response":42,"done":true}',
            b'{"response":"partial","done":false}',
        ):
            with self.subTest(data=data):
                with patch("urllib.request.urlopen", return_value=io.BytesIO(data)):
                    with self.assertRaises(RuntimeError):
                        self.example.generate("hello")

    def test_cli_failure_has_nonzero_status_and_no_success_output(self):
        output, errors = io.StringIO(), io.StringIO()
        with patch.object(self.example, "generate", side_effect=RuntimeError("offline")):
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
                self.assertEqual(self.example.main(), 1)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("ERROR: offline", errors.getvalue())


class TestHostedGemmaExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import httpx
            from google import genai
            from google.genai import types
        except ImportError as exc:
            raise unittest.SkipTest(
                "Install examples/gemma/requirements.txt to run real-SDK offline checks."
            ) from exc
        cls.httpx, cls.genai, cls.types = httpx, genai, types
        cls.example = load_example("hosted")

    def client(self, requests, response):
        def handle(request):
            requests.append(request)
            return self.httpx.Response(200, json=response)
        return self.genai.Client(
            api_key="offline-test-not-a-real-key",
            http_options=self.types.HttpOptions(
                client_args={"transport": self.httpx.MockTransport(handle)}
            ),
        )

    def test_text_request_uses_exact_model_and_returns_nonempty_text(self):
        requests = []
        response = {"candidates": [{"content": {"parts": [{"text": " Model text "}]}}]}
        with self.client(requests, response) as client:
            self.assertEqual(
                self.example.generate(client, self.example.MODELS[0], "hello", None),
                "Model text",
            )
        self.assertEqual(len(requests), 1)
        self.assertIn("gemma-4-26b-a4b-it:generateContent", str(requests[0].url))
        body = json.loads(requests[0].content)
        self.assertEqual(body["contents"][0]["parts"][0]["text"], "hello")

    def test_inline_image_request_uses_actual_sdk_serialization(self):
        requests = []
        response = {"candidates": [{"content": {"parts": [{"text": "Image text"}]}}]}
        with tempfile.TemporaryDirectory() as directory:
            image = Path(directory) / "sample.png"
            image.write_bytes(b"\x89PNG\r\n\x1a\n")
            with self.client(requests, response) as client:
                self.assertEqual(
                    self.example.generate(client, self.example.MODELS[1], "describe", image),
                    "Image text",
                )
        self.assertIn("gemma-4-31b-it:generateContent", str(requests[0].url))
        parts = json.loads(requests[0].content)["contents"][0]["parts"]
        self.assertEqual(parts[1]["inlineData"]["mimeType"], "image/png")
        self.assertTrue(parts[1]["inlineData"]["data"])

    def test_empty_model_text_is_not_success(self):
        with self.client([], {}) as client:
            with self.assertRaisesRegex(ValueError, "No text returned"):
                self.example.generate(client, self.example.MODELS[0], "hello", None)

    def test_invalid_image_is_rejected_before_network(self):
        requests = []
        with tempfile.TemporaryDirectory() as directory:
            for name, data in (("bad.txt", b"image"), ("empty.png", b""), ("big.png", b"x" * (5 * 1024 * 1024 + 1))):
                image = Path(directory) / name
                image.write_bytes(data)
                with self.subTest(name=name), self.client(requests, {}) as client:
                    with self.assertRaises(ValueError):
                        self.example.generate(client, self.example.MODELS[0], "hello", image)
        self.assertEqual(requests, [])

    def test_missing_key_is_explicit_and_never_opens_client(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(self.example, "load_dotenv"):
            with patch("sys.argv", ["hosted.py"]), patch.object(self.example.genai, "Client") as client:
                errors = io.StringIO()
                with contextlib.redirect_stderr(errors):
                    self.assertEqual(self.example.main(), 1)
                self.assertIn("Set GEMINI_API_KEY", errors.getvalue())
                client.assert_not_called()

    def test_network_failure_has_nonzero_status(self):
        with patch.dict(os.environ, {"GEMINI_API_KEY": "offline-test-not-a-real-key"}, clear=True):
            with patch.object(self.example, "load_dotenv"), patch("sys.argv", ["hosted.py"]):
                with patch.object(self.example.genai, "Client", side_effect=self.httpx.ConnectError("refused")):
                    errors = io.StringIO()
                    with contextlib.redirect_stderr(errors):
                        self.assertEqual(self.example.main(), 1)
                    self.assertIn("connection failed", errors.getvalue())


if __name__ == "__main__":
    unittest.main()

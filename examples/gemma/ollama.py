import json
import sys
import urllib.error
import urllib.request


def generate(prompt: str) -> str:
    request = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps({"model": "gemma4:e2b", "prompt": prompt, "stream": False}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            raise RuntimeError("Model unavailable. Run: ollama pull gemma4:e2b") from exc
        raise RuntimeError(f"Ollama HTTP {exc.code}; inspect the daemon logs and model support.") from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError("Cannot reach Ollama or inference timed out. Start the app/ollama serve and retry.") from exc
    except (ValueError, UnicodeError) as exc:
        raise RuntimeError("Ollama returned invalid JSON; inspect the daemon logs.") from exc
    if not isinstance(result, dict):
        raise RuntimeError("Ollama returned an unexpected response shape.")
    if result.get("error"):
        raise RuntimeError(f"Ollama error: {result['error']}")
    text = result.get("response")
    if not isinstance(text, str) or not text.strip():
        raise RuntimeError("Ollama returned no text; inspect the response and daemon logs.")
    if result.get("done") is not True:
        raise RuntimeError("Ollama did not complete generation.")
    return text.strip()


def main() -> int:
    try:
        print(generate("Explain open-source software in one sentence."))
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

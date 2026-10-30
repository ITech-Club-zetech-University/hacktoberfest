import argparse
import os
from pathlib import Path
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import errors, types
import httpx


MODELS = ("gemma-4-26b-a4b-it", "gemma-4-31b-it")
MAX_IMAGE_BYTES = 5 * 1024 * 1024


def generate(client: genai.Client, model: str, prompt: str, image: Path | None) -> str:
    parts = [types.Part.from_text(text=prompt)]
    if image is not None:
        mime_type = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}.get(
            image.suffix.lower()
        )
        if mime_type is None:
            raise ValueError("Use a JPEG or PNG image.")
        with image.open("rb") as source:
            data = source.read(MAX_IMAGE_BYTES + 1)
        if not data or len(data) > MAX_IMAGE_BYTES:
            raise ValueError("Use a non-empty image no larger than 5 MiB (this example's limit).")
        parts.append(types.Part.from_bytes(data=data, mime_type=mime_type))
    response = client.models.generate_content(model=model, contents=parts)
    if not response.text or not response.text.strip():
        raise ValueError("No text returned. Check response safety/finish information before retrying.")
    return response.text.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Backend-only Gemma 4 text/image example.")
    parser.add_argument("--model", choices=MODELS, default=MODELS[0])
    parser.add_argument("--prompt", default="Explain open-source software in one sentence.")
    parser.add_argument("--image", type=Path)
    args = parser.parse_args()
    load_dotenv(Path(__file__).with_name(".env"))
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key or key == "replace_with_your_api_key":
        print("ERROR: Set GEMINI_API_KEY in your environment or private .env.", file=sys.stderr)
        return 1
    try:
        with genai.Client(api_key=key, http_options=types.HttpOptions(timeout=60000)) as client:
            text = generate(client, args.model, args.prompt, args.image)
    except errors.APIError as exc:
        print(f"ERROR: Gemma API status {exc.code}. Check access, model, quota and billing.", file=sys.stderr)
        return 1
    except httpx.HTTPError:
        print("ERROR: Hosted connection failed or timed out. Check connectivity and provider status.", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

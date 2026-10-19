---
title: "3. Multimodal Campus Companion"
parent: Challenges
nav_order: 3
description: "Build an assistant that uses Gemma's native vision or audio understanding to solve a real physical campus challenge."
---

# Challenge 3: Multimodal Campus Companion
{: .no_toc }

**Track focus:** Native vision or audio understanding · **Target window:** ~8 hours · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## 1. Pitch & target user

Real campus life does not happen exclusively in text boxes. Students take photos of lecture whiteboards, scan handwritten timetable changes on notice boards, inspect complicated lab wiring setups, or record voice memos during revision. In this track, your team builds a functional assistant that accepts **genuine non-text input modalities**—specifically images (or audio where supported)—and uses Gemma to perceive, reason about, and explain that input.

- **Target user:** Zetech University students, faculty, campus visitors, or visually impaired peers who need fast, accurate comprehension of physical or visual campus materials.
- **The golden rule:** A text-only chatbot is **strictly not multimodal**. Feeding text transcripts into a chat prompt does not qualify. Gemma must directly consume and analyze visual or auditory media.

## 2. Problem to solve

Students and campus community members frequently waste time or struggle with visual and audio information:
- **Notice board & schedule extraction:** Converting a photo of a handwritten or printed exam reschedule posted on a physical notice board into structured calendar events.
- **Lab apparatus & circuit debugging:** Taking a photo of a breadboard, microcontroller setup, or chemistry lab apparatus and getting an explanation of connections or safety checks.
- **Visual accessibility:** Assisting visually impaired students by describing diagrams, slide deck charts, or lab equipment out loud with plain-language explanations.
- **Terminal & code error diagnostics:** Uploading a screenshot of a terminal stack trace or IDE compile error and receiving a contextual explanation of why the crash occurred and how to fix it.

## 3. Minimum viable project (MVP)

A successful MVP for this track requires:
1. An application capable of receiving at least one non-text file input (e.g. PNG, JPEG, WEBP image, or supported audio recording).
2. Integration with a multimodal Gemma model (accessed via the [Gemini API](https://mlh.link/gemma-quickstart) or a local multimodal runtime) where Gemma directly processes the media tensor/bytes.
3. A functional user interface (web app, mobile app, or CLI tool with image path flags) that accepts the file, invokes Gemma, and displays a grounded text explanation.
4. A safe fallback mechanism that detects and gracefully handles corrupt files, unsupported formats, or ambiguous visual inputs.

## 4. Required Gemma contribution

Gemma is the multimodal perceptual engine:
- **What Gemma does:** Gemma receives the image or audio input alongside the user prompt, performs feature extraction and visual reasoning internally, and outputs synthesized, grounded text.
- **How judges inspect it:** Judges will inspect the API call or model inference loop in your source code to confirm that media data (base64 image bytes, file URI, or audio buffer) is directly passed to the Gemma model. Judges will submit a real test image during the demo to confirm that the model's output changes based on the visual contents of the uploaded file.

## 5. Mandatory acceptance criteria

Every valid entry in this track must pass these four observable tests:

1. **Active non-text modality:** The application successfully ingests at least one genuine non-text input format (e.g. image or audio) and passes it directly to a multimodal Gemma model.
2. **Grounded multimodal response:** The generated response accurately references concrete, verifiable visual elements from the input file (such as specific text on a whiteboard, colors of wires, or labels on a chart).
3. **Graceful invalid-input handling:** When supplied with an unsupported file extension, a corrupted image, or an excessively large file, the application displays a friendly, clear error message without crashing.
4. **Transparent limitation disclosure:** The repository `README.md` clearly lists the exact supported file formats (e.g. JPEG, PNG), maximum file size (e.g. 10 MB), exact Gemma model name, and documented operational limitations (e.g., poor performance in low-light photography or complex handwriting).

## 6. Suggested 2-minute demo scenario

When presenting your multimodal companion to judges, follow this demo flow:

- **0:00 – 0:30 (Problem & Setup):** Explain your campus use case. State which modality your application uses (e.g. image understanding) and identify the specific multimodal Gemma model powering it.
- **0:30 – 1:15 (The Primary Media Demo):** Upload or capture a real campus test image (e.g. a photo of a handwritten lecture schedule, code error screenshot, or circuit diagram included in your repo's `examples/` folder). Submit the query and show Gemma generating a grounded, structured answer.
- **1:15 – 1:45 (Fallback & Edge Case):** Submit an invalid input (e.g., a text file renamed to `.png`, a completely black/blurry image, or an oversized file). Show that the application catches the error gracefully and guides the user on how to fix it.
- **1:45 – 2:00 (Code Inspection):** Show judges the 10–20 lines of code where the image file is encoded and sent to the Gemma API, proving that the multimodal reasoning is performed natively by Gemma.

## 7. Required repository & README evidence

Your public GitHub repository must include:
- [ ] A `README.md` containing:
  - User problem, campus scenario, target audience, and explicit declaration of this track as your team's primary iTech Club challenge track.
  - Exact Gemma model name used (e.g. multimodal Gemma variant via Gemini API) and acknowledgment of the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
  - Explicit list of supported media formats (e.g. PNG, JPEG) and maximum upload sizes.
  - Step-by-step instructions to install dependencies and run the application.
  - Documented model limitations and failure modes.
  - AI tool usage disclosure for any coding assistants used during the event.
- [ ] At least 2–3 sample test media files stored in an `examples/` or `assets/` directory so judges can test the app immediately.
- [ ] Full source code with proper error handling.
- [ ] An OSI-approved open-source `LICENSE` file.

## 8. Stretch goals (optional)

These optional enhancements will distinguish advanced entries but are **not** required to pass:
- **Live camera capture:** Allow users to snap a photo directly from their smartphone or laptop webcam in real time.
- **Multi-image reasoning:** Support comparing two images (e.g. "before" and "after" an experiment, or comparing two conflicting schedule sheets).
- **Audio accessibility:** Integrate text-to-speech output so the generated description can be played aloud for visually impaired users.
- **OCR cross-validation:** Display side-by-side verification of extracted text against the original image regions.

## 9. Starter resources

- [Gemma Quickstart via Gemini API](https://mlh.link/gemma-quickstart) — Setting up multimodal API calls
- [Gemma Image Understanding Guide](https://ai.google.dev/gemma/docs/capabilities/vision/image) — Official documentation for image inputs
- [Gemma Audio Capabilities Guide](https://ai.google.dev/gemma/docs/capabilities/audio) — Handling audio data with Gemma
- [Google AI Studio](https://aistudio.google.com) — Testing multimodal prompts and image uploads interactively
- [Gemma Cookbook `apps/`](https://github.com/google-gemma/cookbook/tree/main/apps) — Worked examples of multimodal applications

## 10. Privacy, safety & licensing

- **Open-source software license:** Your application code must carry an OSI-approved license (e.g., MIT, Apache-2.0). The underlying model is governed separately by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
- **Informed consent:** Do not photograph students, lecturers, or campus staff without their explicit verbal or written permission. Focus your test media on physical artifacts, whiteboards, code screens, or public signage.
- **Sensitive documents:** Never use or upload photos of student identification cards, private exam papers, or confidential university documents.
- **Image copyright:** Ensure all sample images in your repository are captured by your team or taken from permissible creative commons / public domain sources.

## 11. Challenge-specific evaluation notes

These notes supplement the 100-point rubric in [`judging.md`]({{ site.baseurl }}/judging/):
- **Genuine multimodal verification (under Use of Gemma):** Judges will verify that Gemma itself processes the visual/auditory tokens. Projects that simply use third-party OCR to extract text and feed plain strings into a text-only Gemma prompt do not fulfill the spirit of this track.
- **Grounded accuracy (under Technical Execution):** Judges will verify that the answer is tightly grounded in the provided image. The team should demonstrate that changing the input image produces a correspondingly different and accurate response.

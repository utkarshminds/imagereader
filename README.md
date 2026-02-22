# Image Captioning Streamlit App

This Streamlit app lets a user upload an image and generates a short caption. It prefers using Google Cloud services (Vision API + Gemini / Generative Language API) when `GOOGLE_API_KEY` is set, and falls back to a local Hugging Face image-captioning model when no key is provided.

Files:
- `streamlit_app.py` — the Streamlit application.
- `requirements.txt` — Python dependencies.

Usage:

1. (Optional) Create and activate a Python virtual environment.

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. To use Google Vision + Gemini:
- Set `GOOGLE_API_KEY` (API key with access to Vision API and Generative Language API):

Windows (PowerShell, current session):
```powershell
$env:GOOGLE_API_KEY = "YOUR_API_KEY"
```

You can also set `GOOGLE_GEMINI_MODEL` to a different model name (default `text-bison-001`).

4. Run the app:
```bash
streamlit run streamlit_app.py
```

Notes:
- If you don't provide a `GOOGLE_API_KEY`, the app attempts to use a local HF model `nlpconnect/vit-gpt2-image-captioning`. Installing `torch` can be slow and large.
- This repository does not include Google Cloud credentials; you must provide your own API key.
# imagereader
Gemini AI image reader and captioning project

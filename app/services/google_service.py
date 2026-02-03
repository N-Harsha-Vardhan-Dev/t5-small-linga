import os
from google import genai

def google_correct(text: str) -> str:
    api_key = os.getenv("GOOGLE_API_KEY")
    print("Using Google Service with API Key:", api_key)
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Correct the grammar of the following text:\n{text}"
    )

    return response.text.strip()

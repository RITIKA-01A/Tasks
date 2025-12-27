# app.py
from fastapi import FastAPI
import requests

from dotenv import load_dotenv
import os

load_dotenv()   # loads .env into environment

API_KEY = os.getenv("GEMINI_API_KEY")
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"


app = FastAPI()

@app.post("/generate")
def generate(prompt: str, debug: bool = False):
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    res = requests.post(
        f"{URL}?key={API_KEY}",
        headers={"Content-Type": "application/json"},
        json=payload,
    )

    data = res.json()
    return data

    # # SAFETY CHECK FIRST
    # if "candidates" not in data:
    #     return {
    #         "error": "Gemini API error",
    #         "details": data
    #     }

    # # SAFE TO ACCESS NOW
    # text = data["candidates"][0]["content"]["parts"][0]["text"]

    # return {
    #     "response": text,
    #     "raw": data if debug else None
    # }

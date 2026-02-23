import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"


headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def summarize_text(text: str) -> str:
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 150,
            "min_length": 40
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.text}")

    result = response.json()
    return result[0]["summary_text"]

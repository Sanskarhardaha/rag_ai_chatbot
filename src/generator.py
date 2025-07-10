import together
import os
from dotenv import load_dotenv

#  Load .env file
load_dotenv()

#  Set Together API key securely
together.api_key = os.getenv("TOGETHER_API_KEY")

def load_llm():
    return together_completion

def together_completion(prompt: str) -> str:
    response = together.Complete.create(
        prompt=prompt,
        model="mistralai/Mistral-7B-Instruct-v0.1",
        max_tokens=512,
        temperature=0.7,
        stop=["</s>"]
    )
    return response['choices'][0]['text'].strip()

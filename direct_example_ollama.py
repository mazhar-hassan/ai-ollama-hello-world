import requests
from urllib3 import request

#ollama serve
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b"

def query_ollama(promot, model = MODEL_NAME, stream = False):
    payload = {
        "model": model,
        "prompt": promot,
        "stream": stream
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "[No response received]")
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {e}"


print (query_ollama("What is the future of AI?"))

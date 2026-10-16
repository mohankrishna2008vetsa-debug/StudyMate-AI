
import requests
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen3:4b-instruct"


def ask_ai(prompt):
    skill_path = Path(__file__).with_name("skill.md")

    if not skill_path.exists():
        raise FileNotFoundError("skill.md was not found.")

    system_prompt = skill_path.read_text(encoding="utf-8")

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "options": {"temperature": 0.4}
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]

    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Cannot connect to Ollama. Please open the Ollama app."
        )
    except requests.exceptions.Timeout:
        raise RuntimeError("The AI took too long to respond. Try again.")
    except requests.exceptions.HTTPError as error:
        raise RuntimeError(
            f"Ollama returned an error: {error}. "
            "Check whether the model is installed."
        )
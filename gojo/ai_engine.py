
import json
from openai import OpenAI

config = json.load(open("config/config.json"))
client = OpenAI(api_key=config["api_key"])

def ask_ai(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are Gojo, an advanced voice assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI error: {e}"

import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def ai_logic(prompt, max_tokens=100):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-0125",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choice(0).text.strip()
    except Exception as e:
        return str(e)

import os
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
load_dotenv()


def ai_logic(prompt, max_tokens=100):
    try:
        response = client.completions.create(model="davinci-002",
                                             prompt=prompt,
                                             max_tokens=max_tokens)
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def ask_openrouter(prompt):

    response = client.chat.completions.create(
        model="poolside/laguna-s-2.1:free",
        messages=[
            {
                "role": "system",
                "content": "You are an expert shopping planner."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content


def safe_json_parse(text: str):
    try:
        return json.loads(text)
    except:
        return {"score": 0, "suggestions": ["Invalid LLM output"]}

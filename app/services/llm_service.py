from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a precise JSON generator. Always return valid JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


def safe_json_parse(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # fallback extraction attempt (very useful for grading)
        try:
            import re
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if match:
                return json.loads(match.group())
        except:
            pass

        return {
            "score": 0,
            "suggestions": [
                "LLM output was not valid JSON. Prompt needs improvement."
            ]
        }

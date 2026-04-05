from dotenv import load_dotenv
import os
from openai import OpenAI
import json
from app.tools.scraper import scrape_job_description

# Load API key
load_dotenv()

client = OpenAI()

def analyze_resume_and_jd(resume_text: str, job_url: str):
    jd_text = scrape_job_description(job_url)

    prompt = f"""
You are a career coach.

Analyze the resume against the job description.

STRICT RULES:
- Return ONLY valid JSON
- No explanation
- No extra text

Format:
{{
  "score": integer (0-100),
  "suggestions": ["string", "string"]
}}

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    output = response.choices[0].message.content

    print("RAW OUTPUT:", output)  # debug

    try:
        return json.loads(output)
    except Exception as e:
        print("ERROR:", e)
        return {
            "score": 0,
            "suggestions": ["Failed to parse AI response"]
        }


from app.tools.scraper_tool import scrape_job_tool
from app.schemas.resume_score import ResumeScore
import json

def analyze_resume(resume_text: str, job_url: str, llm_call_fn):
    # 1. Scrape job description
    job_text = scrape_job_tool(job_url)

    # 2. Build prompt (agent reasoning layer)
    prompt = f"""
You are an expert recruiter.

Evaluate this candidate.

Return ONLY valid JSON.

Resume:
{resume_text}

Job Description:
{job_text}

JSON format:
{{
  "score": 0-100,
  "strengths": ["..."],
  "suggestions": ["..."]
}}
"""

    # 3. Call LLM
    response = llm_call_fn(prompt)

    # 4. Parse output safely
    try:
        data = json.loads(response)
        return ResumeScore(**data)
    except Exception:
        return {"error": "Invalid LLM response", "raw": response}

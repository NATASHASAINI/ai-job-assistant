def resume_prompt(resume, job):
    return f"""
You are a recruiter.

Return ONLY JSON:
{{
  "score": 0-100,
  "suggestions": []
}}

RESUME:
{resume}

JOB:
{job}
"""


def tailored_prompt(profile, job, question):
    return f"""
You are a career coach.

Write a strong answer.

PROFILE:
{profile}

JOB:
{job}

QUESTION:
{question}

Return only final answer.
"""

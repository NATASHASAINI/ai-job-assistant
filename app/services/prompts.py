RESUME_SCORE_PROMPT = """
You are an expert recruiter.

Compare resume with job description.

Return STRICT JSON only:

{
  "score": <integer 0-100>,
  "suggestions": [<string>, <string>]
}

Resume:
{resume}

Job Description:
{job}
"""

TAILORED_ANSWER_PROMPT = """
You are a career coach.

Write a strong professional answer to:

Question: {question}

Based on:
Profile: {profile}
Job Description: {job}

Keep it concise and compelling.
"""

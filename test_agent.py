from app.agents.resume_agent import analyze_resume

def mock_llm(prompt):
    return """
    {
        "score": 82,
        "strengths": ["Python", "FastAPI"],
        "suggestions": ["Add ML projects", "Improve system design"]
    }
    """

resume = "Python developer with FastAPI experience"
url = "https://jobs.lever.co/openai"

result = analyze_resume(resume, url, mock_llm)

print(result)

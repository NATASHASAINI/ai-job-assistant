# app/api.py
from fastapi import FastAPI
from app.agents.resume_scorer import analyze_resume_and_jd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AI Job Assistant API is running"}

# Example endpoint for testing resume scoring
@app.post("/analyze_resume")
async def analyze_resume_endpoint(resume: str, job_url: str):
    result = analyze_resume_and_jd(resume, job_url)
    return result


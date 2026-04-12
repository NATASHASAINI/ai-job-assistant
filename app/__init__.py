from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agents.resume_scorer import analyze_resume_and_jd

app = FastAPI(title="AI Job Assistant API")

class ResumeRequest(BaseModel):
    resume_text: str
    job_url: str

@app.post("/analyze_resume")
async def analyze_resume(request: ResumeRequest):
    try:
        result = analyze_resume_and_jd(request.resume_text, request.job_url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to AI Job Assistant API"}


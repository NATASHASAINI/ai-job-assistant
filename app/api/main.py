from fastapi import FastAPI
from app.services.agent import resume_score, generate_answer

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI Job Assistant running"}

@app.post("/resume-score")
def score(data: dict):
    return resume_score(data["resume"], data["job_url"])

@app.post("/answer")
def answer(data: dict):
    return generate_answer(
        data["profile"],
        data["job_url"],
        data["question"]
    )

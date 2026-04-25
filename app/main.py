from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup
import openai
import json
import os

# =========================
# FASTAPI APP
# =========================
app = FastAPI()


# =========================
# CONFIG
# =========================
openai.api_key = os.getenv("OPENAI_API_KEY")


# =========================
# DATA CONTRACTS
# =========================

class ResumeScoreRequest(BaseModel):
    resume_text: str
    job_url: str


class AnswerRequest(BaseModel):
    profile: Dict[str, Any]
    job_url: str
    question: str


class ResumeScoreOutput(BaseModel):
    score: int
    suggestions: List[str]


# =========================
# SCRAPER TOOL
# =========================

def scrape_job_description(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    clean_text = " ".join(text.split())
    return clean_text[:12000]


# =========================
# LLM CALL
# =========================

def call_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert career AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"]


# =========================
# PROMPTS (FEW-SHOT STYLE)
# =========================

def build_resume_score_prompt(resume: str, job: str) -> str:
    return f"""
You are a resume evaluator.

Return ONLY valid JSON:
{{
  "score": integer (0-100),
  "suggestions": [string]
}}

Example:
Resume: Python, ML
Job: Python, ML, AWS
Output:
{{"score": 85, "suggestions": ["Add AWS experience"]}}

NOW:

Resume:
{resume}

Job:
{job}
"""


def build_answer_prompt(profile: dict, job: str, question: str) -> str:
    return f"""
You are a senior career coach.

PROFILE:
{json.dumps(profile)}

JOB:
{job}

QUESTION:
{question}

Write a strong, natural answer. No fluff.
"""


# =========================
# PARSER
# =========================

def parse_score(raw: str) -> ResumeScoreOutput:
    try:
        data = json.loads(raw)
        return ResumeScoreOutput(**data)
    except:
        return ResumeScoreOutput(score=0, suggestions=["Failed to parse LLM output"])


# =========================
# AGENTS
# =========================

def resume_scorer(resume_text: str, job_url: str):
    job = scrape_job_description(job_url)
    prompt = build_resume_score_prompt(resume_text, job)
    raw = call_llm(prompt)
    return parse_score(raw)


def generate_answer(profile: dict, job_url: str, question: str):
    job = scrape_job_description(job_url)
    prompt = build_answer_prompt(profile, job, question)
    return call_llm(prompt)


# =========================
# ROOT ROUTE
# =========================

@app.get("/")
def home():
    return {"status": "AI Job Assistant Running"}


# =========================
# API ROUTES
# =========================

@app.post("/resume-score")
def score(req: ResumeScoreRequest):
    return resume_scorer(req.resume_text, req.job_url).dict()


@app.post("/answer")
def answer(req: AnswerRequest):
    return {
        "answer": generate_answer(req.profile, req.job_url, req.question)
    }

from pydantic import BaseModel
from typing import List

class ResumeScoreRequest(BaseModel):
    resume: str
    job_url: str


class AnswerRequest(BaseModel):
    profile: dict
    job_url: str
    question: str


class ResumeScoreResponse(BaseModel):
    score: int
    suggestions: List[str]

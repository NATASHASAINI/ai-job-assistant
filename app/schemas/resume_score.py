from pydantic import BaseModel
from typing import List

class ResumeScore(BaseModel):
    score: int
    strengths: List[str]
    suggestions: List[str]


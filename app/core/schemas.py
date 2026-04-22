from typing import List, Dict, Any

UserProfile = Dict[str, Any]

ResumeScoreOutput = {
    "score": int,
    "suggestions": List[str]
}

from pydantic import BaseModel


class MatchResult(BaseModel):

    overall_score: int = 0

    matched_skills: list[str] = []

    missing_skills: list[str] = []

    strengths: list[str] = []

    weaknesses: list[str] = []

    suggestions: list[str] = []
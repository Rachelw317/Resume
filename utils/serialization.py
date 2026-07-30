from schemas.resumeTemplate import Resume
from schemas.jd import JD
from schemas.match import MatchResult


def resume_from_json(data: str) -> Resume:
    return Resume.model_validate_json(data)


def jd_from_json(data: str) -> JD:
    return JD.model_validate_json(data)


def match_from_json(data: str) -> MatchResult:
    return MatchResult.model_validate_json(data)
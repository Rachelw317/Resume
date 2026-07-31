from langchain.tools import tool

from utils.serialization import (
    resume_from_json,
    jd_from_json,
    match_from_json
)

from core.resume_optimizer import optimize_resume
@tool
def optimize_resume_tool(
    resume_json: str,
    jd_json: str,
    match_json: str
) -> str:
    """
    根据 JD 和 MatchResult 优化简历。
    返回 OptimizedResume JSON。
    """
    resume = resume_from_json(resume_json)
    jd = jd_from_json(jd_json)
    match = match_from_json(match_json)

    optimized_resume = optimize_resume(
        resume,
        jd,
        match
    )
    return optimized_resume.model_dump_json()

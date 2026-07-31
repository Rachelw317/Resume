from langchain.tools import tool


from utils.serialization import (
    resume_from_json,
    jd_from_json
)

from core.match_analyzer import analyze_match
@tool
def analyze_match_tool(
    resume_json: str,
    jd_json: str
) -> str:
    """
    分析 Resume 与 JD 的匹配情况。
    返回 MatchResult JSON。
    """

    resume = resume_from_json(resume_json)

    jd = jd_from_json(jd_json)

    match = analyze_match(
        resume,
        jd
    )

    return match.model_dump_json()

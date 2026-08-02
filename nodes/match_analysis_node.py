from schemas.state import ResumeState
from core.match_analyzer import analyze_match

def match_analysis_node(state: ResumeState) -> dict:
    """
    Node for analyzing the match between resume and job description.
    """
    if state.resume is None or state.jd is None:
        state.error = "Resume or Job Description data is missing."
        return {"error": state.error}

    try:
        match_result = analyze_match(state.resume, state.jd)
        state.match_result = match_result
        return {"match_result": match_result}
    except Exception as e:
        state.error = str(e)
        return {"error": state.error}
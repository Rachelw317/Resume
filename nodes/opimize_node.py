from core.resume_optimizer import optimize_resume
from schemas.state import ResumeState

def optimize_resume_node(state: ResumeState) -> dict:
    """
    Node for optimizing the resume based on the job description and match analysis.
    """
    if state.resume is None or state.jd is None or state.match_result is None:
        state.error = "Resume, Job Description, or Match Result data is missing."
        return {"error": state.error}

    try:
        optimized_resume = optimize_resume(state.resume, state.jd, state.match_result)
        state.optimized_resume = optimized_resume
        return {"optimized_resume": optimized_resume}
    except Exception as e:
        state.error = str(e)
        return {"error": state.error}
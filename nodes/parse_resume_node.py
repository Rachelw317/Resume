from schemas.state import ResumeState
from core.resume_parser import parse_resume

def parse_resume_node(state: ResumeState) -> dict:
    """
    Parse resume text and update the state with the parsed information.
    """
    if state.resume_text:
        try:
            resume = parse_resume(state.resume_text)
            return {"resume": resume}
        except Exception as e:
            return {"error": f"Failed to parse resume: {str(e)}"}
    return {"error": "Resume text is not available for parsing."}
   
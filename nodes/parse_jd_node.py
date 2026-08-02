from schemas.state import ResumeState
from core.jd_parser import parse_jd

def parse_jd_node(state: ResumeState) -> dict:
    """
    Parse JD text and update the state with the parsed information.
    """
    if state.jd_text:
        try:
            jd = parse_jd(state.jd_text)
            return {"jd": jd}
        except Exception as e:
            return {"error": f"Failed to parse JD: {str(e)}"}
    return {"error": "JD text is not available for parsing."}
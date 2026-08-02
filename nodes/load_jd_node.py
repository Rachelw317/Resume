from schemas.state import ResumeState
from loaders.jd_loader import load_jd

def load_jd_node(state: ResumeState) -> dict:
    """
    Load JD from file and update the state with the extracted text.
    """
    if state.jd_file_path:
        try:
            jd_text = load_jd(state.jd_file_path)
            return {"jd_text": jd_text}
        except Exception as e:
            return {"error": f"Failed to load JD: {str(e)}"}
    return {"error": "JD file path is not provided."}
    
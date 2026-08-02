from schemas.state import ResumeState
from loaders.file_loader import load_resume

def load_resume_node(state: ResumeState) -> dict:
    """
    Load resume from file and update the state with the extracted text.
    """
    if state.resume_file_path:
        try:
            resume_text = load_resume(state.resume_file_path)
            return {"resume_text": resume_text}
        except Exception as e:
            return {"error": f"Failed to load resume: {str(e)}"}
    return {"error": "Resume file path is not provided."}

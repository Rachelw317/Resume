from schemas.state import ResumeState
from tools.markdown_writer import write_markdown

def write_node(state: ResumeState) -> dict:
    """
    Node for writing the optimized resume to a markdown file.
    """
    if state.optimized_resume is None:
        state.error = "Optimized resume data is missing."
        return {"error": state.error}

    try:
        output_path = "./outputs/optimized_resume.md"
        write_markdown(state.optimized_resume, output_path)
        return {"message": f"Optimized resume written to {output_path}"}
    except Exception as e:
        state.error = str(e)
        return {"error": state.error}
from langchain.tools import tool

@tool
def GenerateJobDescription (JD: str) -> str:
    """Get Precise job description based on the job you privide."""
    return f""
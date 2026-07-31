from langchain.tools import tool

from utils.serialization import (
    resume_from_json
)


from tools.markdown_writer import write_markdown
@tool
def write_markdown_tool(optimized_resume_json: str) -> str:
    """
    将优化后的简历写入 Markdown 文件。
    返回 Markdown 文件路径。
    """
    optimized_resume = resume_from_json(optimized_resume_json)

    output_path = "./outputs/optimized_resume.md"

    write_markdown(
        optimized_resume,
        output_path
    )

    return output_path
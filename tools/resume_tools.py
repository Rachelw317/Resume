from langchain.tools import tool


from loaders.file_loader import load_resume
@tool
def load_resume_tool(
    file_path:str
)->str:
    """
    读取用户上传的简历文件。

    适用于：
    - PDF格式简历
    - DOCX格式简历

    不要用于：
    - JD
    - 职位描述
    - TXT文件
    """

    print("DEBUG file_path =", repr(file_path))

    text = load_resume(file_path)

    return text


from core.resume_parser import parse_resume
@tool
def parse_resume_tool(resume_text: str) -> str:
    """
    将简历文本解析为结构化 Resume。
    返回 JSON 字符串。
    """

    resume = parse_resume(resume_text)

    return resume.model_dump_json()


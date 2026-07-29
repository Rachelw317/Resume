from langchain.tools import tool

from loaders.file_loader import load_resume



@tool
def load_resume_tool(file_path:str)->str:
    """
    读取PDF或Word格式的简历文件，
    返回简历文本。
    """

    text = load_resume(file_path)

    return text
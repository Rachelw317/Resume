from langchain.tools import tool

from core.jd_parser import parse_jd
@tool
def parse_jd_tool(file_path: str) -> str:
    """
    读取岗位描述文件。

    输入:
    - txt格式的岗位描述文件内容

    不可以用于:
    - 简历文件
    """

    with open(file_path, "r", encoding="utf-8") as f:
        jd_text = f.read()

    jd = parse_jd(jd_text)

    return jd.model_dump_json()

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


from core.resume_parser import parse_resume
@tool
def parse_resume_tool(resume_text: str) -> str:
    """
    将简历文本解析为结构化 Resume。
    返回 JSON 字符串。
    """

    resume = parse_resume(resume_text)

    return resume.model_dump_json()


from core.jd_parser import parse_jd
@tool
def parse_jd_tool(jd_text: str) -> str:
    """
    将 JD 文本解析为结构化 JD。
    返回 JSON 字符串。
    """

    jd = parse_jd(jd_text)

    return jd.model_dump_json()



from utils.serialization import (
    resume_from_json,
    jd_from_json,
    match_from_json
)

from core.match_analyzer import analyze_match
@tool
def analyze_match_tool(
    resume_json: str,
    jd_json: str
) -> str:
    """
    分析 Resume 与 JD 的匹配情况。
    返回 MatchResult JSON。
    """

    resume = resume_from_json(resume_json)

    jd = jd_from_json(jd_json)

    match = analyze_match(
        resume,
        jd
    )

    return match.model_dump_json()


from core.resume_optimizer import optimize_resume
@tool
def optimize_resume_tool(
    resume_json: str,
    jd_json: str,
    match_json: str
) -> str:
    """
    根据 JD 和 MatchResult 优化简历。
    返回 OptimizedResume JSON。
    """
    resume = resume_from_json(resume_json)
    jd = jd_from_json(jd_json)
    match = match_from_json(match_json)

    optimized_resume = optimize_resume(
        resume,
        jd,
        match
    )
    return optimized_resume.model_dump_json()


from tools.markdown_writer import write_markdown
@tool
def write_markdown_tool(optimized_resume_json: str) -> str:
    """
    将优化后的简历写入 Markdown 文件。
    返回 Markdown 文件路径。
    """
    optimized_resume = resume_from_json(optimized_resume_json)

    output_path = "./output/optimized_resume.md"

    write_markdown(
        optimized_resume,
        output_path
    )

    return output_path
    
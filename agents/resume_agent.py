from tools.resume_tools import load_resume_tool, parse_resume_tool
from tools.jd_tools import parse_jd_tool
from tools.match_tools import analyze_match_tool
from tools.optimizer_tools import optimize_resume_tool
from tools.output_tools import write_markdown_tool
from langchain.agents import create_agent

agent = create_agent(
    model="deepseek-chat",
    tools=[
        load_resume_tool,
        parse_resume_tool,
        parse_jd_tool,
        analyze_match_tool,
        optimize_resume_tool,
        write_markdown_tool
    ],
    system_prompt=
    """
    你是一个简历优化助手。

    规则：

    1. PDF/DOCX文件只能使用load_resume_tool
    2. 后缀名为txt的岗位描述只能使用parse_jd_tool
    3. 不允许使用load_resume_tool读取TXT文件
    4. 读取JD内容时使用parse_jd_tool，用来获取准确JD内容。
    """
)

from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from tools.resume_tools import (
    load_resume_tool,
    parse_resume_tool,
    parse_jd_tool,
    analyze_match_tool,
    optimize_resume_tool,
)

tools = [
    load_resume_tool,
    parse_resume_tool,
    parse_jd_tool,
    analyze_match_tool,
    optimize_resume_tool,
]

def get_llm():
    from core.model import get_deepseek
    return get_deepseek()

llm = get_llm()

prompt = PromptTemplate.from_template(
    """你是一个简历优化专家，帮助用户分析简历与JD的匹配情况，并优化简历，使其更符合JD的要求。

你可以使用以下工具：
{tools}

工具名称：
{tool_names}

问题：
{input}

{agent_scratchpad}"""
)

react_agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent = AgentExecutor(agent=react_agent, tools=tools, verbose=True)

from core.model import get_deepseek
from tools.resume_tools import load_resume_tool, parse_resume_tool
from langchain.agents import create_agent

agent = create_agent(
    model="deepseek-chat",
    tools=[
        load_resume_tool,
        parse_resume_tool,
    ]
)

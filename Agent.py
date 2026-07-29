from langchain.agents import create_agent
from Tool import tools
from Model import get_DeepSeek

agent = create_agent(
    model = get_DeepSeek(),
    tools = tools
    system_prompt = "你是一个有用的助手，善于用工具解决问题。"
)
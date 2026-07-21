from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from llm_config import get_llm
load_dotenv()



messages = [
    SystemMessage(content="你是一个耐心的 Python 老师，回答要简短。"),
    HumanMessage(content="用一句话解释什么是变量？"),
]

llm = get_llm()

response = llm.invoke(messages)
print(response.content)
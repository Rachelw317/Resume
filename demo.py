from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv()


llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0
)

response = llm.invoke("介绍一下 LangChain")
print(response.content)
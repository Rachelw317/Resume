import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv()

# 设置默认模型
DEFAULT_MODEL = "deepseek-chat"

def get_DeepSeek(model: str = DEFAULT_MODEL) -> ChatDeepSeek:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "未找到API_KEY。"
        )
    return ChatDeepSeek(model = model, api_key=api_key)
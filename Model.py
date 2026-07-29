import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse

load_dotenv()

# 增加中间件动态切换模型
basic_model = "deepseek-v4-flash"
advanced_model = "deepseek-v4-pro"

@wrap_model_call
def dynamic_model_call(request: ModelRequest, handler) -> ModelResponse:
    if len(request.state["messages"]) > 10:
        return handler(request.override(model = advanced_model))
    return handler(request.override(model = basic_model))

def get_DeepSeek(model: str = DEFAULT_MODEL) -> ChatDeepSeek:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "未找到API_KEY。"
        )
    return ChatDeepSeek(model = model, api_key=api_key)
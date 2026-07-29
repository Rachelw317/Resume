from langchain.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

system_msg = SystemMessage("你是一位资深Python开发者")
human_msg = HumanMessage("如何创建REST API？")
ai_msg = AIMessage("我来详细解释这个问题。")
messages = [system_msg, human_msg, ai_msg]
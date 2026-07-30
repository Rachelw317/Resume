from agents.resume_agent import agent

file_path = "./tests/测试用简历.docx"

result = agent.invoke(
    {"messages": [{"role": "user", "content": f"我的简历在{file_path}，请帮我解析一下。并返回结构化 JSON。"}]}
)

print(result)

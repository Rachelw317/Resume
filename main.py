from agents.resume_agent import agent

file_path = "./tests/测试用简历.docx"

result = agent.invoke({
    "input": f"请帮我分析这份简历与这份JD的匹配情况，并优化简历，使其更符合JD的要求。我的简历存储在{file_path}中，请帮我分析并优化。"
})

print(result)

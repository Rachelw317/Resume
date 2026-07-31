from agents.resume_agent import agent

file_path = "./tests/测试用简历.docx"
jd_path = "./tests/test_jd.txt"


result = agent.invoke(
    {"messages": [{"role": "user", "content": f"你是一个简历优化专家，擅长根据JD优化简历。我的简历在{file_path}，JD在{jd_path}。请你按照{file_path}，调用工具的同时不要破坏文件存储路径，帮我解析一下简历和JD，并分析匹配度，最后帮我优化简历，并输出优化后的简历Markdown文件路径。"}]}
)

print(result)


# from loaders.file_loader import load_resume

# resume_content = load_resume(file_path)
# print(resume_content)
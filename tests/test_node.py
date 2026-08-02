from nodes.load_resume_node import load_resume_node
from schemas.state import ResumeState


state = ResumeState(resume_file_path="./tests/测试用简历.docx")

result = load_resume_node(state)

print("Resume Text:", result.resume_text)
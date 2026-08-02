from graph.resume_graph import build_resume_graph
from schemas.state import ResumeState


graph = build_resume_graph()

state = ResumeState(
    resume_file_path="./tests/测试用简历.docx",
    jd_file_path="./tests/test_jd.txt"
)

result = graph.invoke(
    state
)


print(result)
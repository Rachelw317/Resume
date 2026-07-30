from tools.markdown_writer import write_markdown
from tools.resume_tools import load_resume_tool

result = load_resume_tool.invoke(
    {
    "file_path": "./tests/测试用简历.docx"
    }
)


print(result)

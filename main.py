from loaders.file_loader import load_resume

from core.resume_parser import parse_resume



text = load_resume(
    "tests/测试用简历.docx"
)


resume = parse_resume(text)


print(resume)

print(resume.skills)
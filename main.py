from loaders.file_loader import load_resume

from core.resume_parser import parse_resume

from core.jd_parser import parse_jd

from core.match_analyzer import analyze_match

from core.resume_optimizer import optimize_resume

from tools.markdown_writer import write_markdown

resume_text = load_resume(
    "./tests/测试用简历.docx"
)


resume = parse_resume(
    resume_text
)



with open(
    "./tests/test_jd.txt",
    encoding="utf-8"
) as f:

    jd_text=f.read()



jd = parse_jd(jd_text)



result = analyze_match(
    resume,
    jd
)


print(result)

optimized_resume = optimize_resume(
    resume,
    jd,
    result
)

output = write_markdown(
    optimized_resume,
    "./outputs/resume_modified.md"
)


print(output)
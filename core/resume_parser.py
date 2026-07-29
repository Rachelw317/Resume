from core.model import get_deepseek
from core.prompt import RESUME_EXTRACTION_PROMPT

from schemas.resumeTemplate import Resume



def parse_resume(text:str)->Resume:

    llm = get_deepseek()

    structured_llm = (
        llm.with_structured_output(
            Resume
        )
    )


    result = structured_llm.invoke(
        RESUME_EXTRACTION_PROMPT.format(
            resume_text=text
        )
    )


    return result
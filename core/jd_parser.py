from core.model import get_deepseek

from core.prompt import JD_EXTRACTION_PROMPT

from schemas.jd import JD



def parse_jd(text:str)->JD:

    llm = get_deepseek()


    structured_llm = (
        llm.with_structured_output(
            JD
        )
    )


    result = structured_llm.invoke(
        JD_EXTRACTION_PROMPT.format(
            jd_text=text
        )
    )


    return result
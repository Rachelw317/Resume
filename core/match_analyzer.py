from core.model import get_deepseek

from core.prompt import MATCH_ANALYSIS_PROMPT

from schemas.match import MatchResult



def analyze_match(
    resume,
    jd
):

    llm = get_deepseek()


    structured_llm = (
        llm.with_structured_output(
            MatchResult
        )
    )


    result = structured_llm.invoke(

        MATCH_ANALYSIS_PROMPT.format(

            resume=resume.model_dump_json(),

            jd=jd.model_dump_json()

        )

    )


    return result
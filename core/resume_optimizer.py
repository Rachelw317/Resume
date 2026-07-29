from core.model import get_deepseek

from core.prompt import (
    RESUME_OPTIMIZATION_PROMPT
)

from schemas.optimized_resume import (
    OptimizedResume
)



def optimize_resume(
    resume,
    jd,
    match
):

    llm = get_deepseek()


    structured_llm = (
        llm.with_structured_output(
            OptimizedResume
        )
    )


    result = structured_llm.invoke(

        RESUME_OPTIMIZATION_PROMPT.format(

            resume=resume.model_dump_json(),

            jd=jd.model_dump_json(),

            match=match.model_dump_json()

        )

    )


    return result
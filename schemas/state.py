# State 保存的是"流程中的共享数据"，而不是所有数据。
# 每个 Node 只负责读自己需要的数据，写自己负责的数据。

from pydantic import BaseModel

from .resumeTemplate import Resume
from .jd import JD
from .match import MatchResult
from .optimized_resume import OptimizedResume


class ResumeState(BaseModel):

    # input files
    resume_file_path: str | None = None
    jd_file_path: str | None = None

    # extracted text
    resume_text: str | None = None
    jd_text: str | None = None

    # parsed data
    resume: Resume | None = None
    jd: JD | None = None

    # analysis result
    match_result: MatchResult | None = None

    # generated result
    optimized_resume: OptimizedResume | None = None
    
    # output
    export_file_path: str | None = None

    # error
    error: str | None = None
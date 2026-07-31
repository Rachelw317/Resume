from pathlib import Path

from .pdf_loader import load_pdf
from .docx_loader import load_docx



def load_resume(file_path:str)->str:

    suffix = Path(file_path).suffix.lower()


    if suffix == ".pdf":
        return load_pdf(file_path)


    elif suffix == ".docx":
        return load_docx(file_path)


    else:
        raise ValueError(
            "Unsupported file format"
        )


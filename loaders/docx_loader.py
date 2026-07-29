from docx import Document


def load_docx(file_path: str) -> str:
    """
    读取docx文件并返回文本
    """

    doc = Document(file_path)

    paragraphs = []

    for para in doc.paragraphs:
        paragraphs.append(
            para.text
        )

    return "\n".join(paragraphs)
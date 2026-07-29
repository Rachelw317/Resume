import fitz


def load_pdf(file_path: str) -> str:
    """
    读取PDF文件并返回文本
    """

    text = ""

    doc = fitz.open(file_path)

    for page in doc:
        text += page.get_text()

    doc.close()

    return text
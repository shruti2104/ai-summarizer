from pypdf import PdfReader


def extract_text_from_pdf(file_path):

    reader = PdfReader(file_path)

    content = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            content += text + "\n"

    if not content.strip():
        raise ValueError(
            "Could not extract text from this PDF"
        )
    return content
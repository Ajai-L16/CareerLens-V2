import pdfplumber
import docx

def extract_text_from_file(file_stream, file_name):
    """Extracts text from a .pdf or .docx file stream."""
    if file_name.endswith('.pdf'):
        with pdfplumber.open(file_stream) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages)
    elif file_name.endswith('.docx'):
        doc = docx.Document(file_stream)
        return "\n".join(para.text for para in doc.paragraphs)
    else:
        return None

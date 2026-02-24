import pdfplumber
import os
from docx import Document


def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()


def extract_resume_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    else:
        raise ValueError("Unsupported file format")


def load_all_resumes(folder_path):
    resumes = {}
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            resumes[file] = extract_resume_text(file_path)
        except Exception as e:
            print(f"Error processing {file}: {e}")
    return resumes
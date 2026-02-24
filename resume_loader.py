import os
from pdf_parser import extract_text_from_pdf

def load_resumes_from_folder(folder_path):
    resumes = {}
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            resumes[file] = extract_text_from_pdf(path)
    return resumes
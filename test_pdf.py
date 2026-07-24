from utils.pdf_parser import extract_text_from_pdf

pdf_path = r"C:\Users\Lenovo\Downloads\Resume (2).pdf"

text = extract_text_from_pdf(pdf_path)

print(text)
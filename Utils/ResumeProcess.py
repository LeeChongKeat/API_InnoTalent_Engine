import PyPDF2
def extract_text_from_resume_pdf(pdf_file_path):
    try:
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            pdf_text = ""
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                pdf_text += page.extractText()
            return pdf_text
    except Exception as e:
        print(f"Error: {e}")
        return None

def check_resume_exist_and_read(pdf_file_path):
    extracted_text = extract_text_from_resume_pdf(pdf_file_path)
    if extracted_text:
        return extracted_text
    else:
        return None
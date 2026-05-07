from app.utils.file_handler import save_uploaded_file
from app.utils.text_extractor import extract_text_from_pdf
from app.services.parsing_service import parse_resume


def process_resume(file):

    # 1. Save file
    file_path = save_uploaded_file(file)

    # 2. Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # 3. AI parsing
    parsed_data = parse_resume(extracted_text)

    return {
        "file_path": file_path,
        "extracted_text": extracted_text,
        "parsed_data": parsed_data
    }
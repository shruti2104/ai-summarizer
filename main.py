from dotenv import load_dotenv
from pypdf import PdfReader
from services.pdf_reader import extract_text_from_pdf
from services.summarizer import summarize_text
import os


load_dotenv()

def summarize_pdf(file_path):

    text = extract_text_from_pdf(file_path)

    result = summarize_text(text)

    return result



# Program starts here

# result = summarize_pdf("Pre-SaleBash.pdf")

# print(result)
# print(summary["summary"])
# print(summary["key_points"])
# print(summary["action_items"])
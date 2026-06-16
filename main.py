from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import os
import json


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)

    content = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            content += text + "\n"

    return content


def summarize_text(text):

    messages = [
        {
            "role": "system",
            "content": """
            You are a document summarizer.

            Return a json object only.

            Format:

            {
              "summary": "",
              "key_points": [],
              "action_items": []
            }

            Rules:
            - Only use information from the document
            - Do not add information
            - Do not give advice
            - Do not infer action items
            """
        },
        {
            "role": "user",
            "content": text
        }
    ]


    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        response_format={
            "type": "json_object"
        },
        messages=messages
    )


    return json.loads(
        response.choices[0].message.content
    )


def summarize_pdf(file_path):

    text = extract_text_from_pdf(file_path)

    result = summarize_text(text)

    return result



# Program starts here

result = summarize_pdf("Pre-SaleBash.pdf")

print(result)
# print(summary["summary"])
# print(summary["key_points"])
# print(summary["action_items"])
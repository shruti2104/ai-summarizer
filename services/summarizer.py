from openai import OpenAI
from dotenv import load_dotenv
import os
import json


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def validate_summary(data):

    required_fields = [
        "summary",
        "key_points",
        "action_items"
    ]

    for field in required_fields:

        if field not in data:
            raise ValueError(
                f"Missing field: {field}"
            )


    return data

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


    result = json.loads(
        response.choices[0].message.content
    )

    return validate_summary(result)
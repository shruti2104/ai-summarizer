import streamlit as st
import uuid
import os
import json
from main import summarize_pdf


st.title("AI PDF Summarizer")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)
    file_name = f"uploads/{uuid.uuid4()}.pdf"
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Summarize"):

        try:

            result = summarize_pdf(file_name)
            st.subheader("Summary")
            st.write(result["summary"])


            st.subheader("Key Points")

            for point in result["key_points"]:
                st.write("•", point)


            st.subheader("Action Items")

            for item in result["action_items"]:
                st.write("•", item)
            
            json_file = json.dumps(
                result,
                indent=2
            )


            st.download_button(
                label="Download Summary",
                data=json_file,
                file_name="summary.json",
                mime="application/json"
            )
       
        except Exception as e:

            st.error(str(e))
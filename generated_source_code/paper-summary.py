import streamlit as st
from PyPDF2 import PdfReader
import docx
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# IBM Granite API credentials
granite_api_key = os.environ.get("WATSONX_API_KEY")
granite_url = "https://api.ibm.com/granite/v1/summarize"

@st.llm_function(creative=False)
async def summarize_paper(paper_text: str, summary_length: str, summary_type: str) -> str:
    """Summarize the research paper into a concise summary using IBM Granite."""
    # Set up the API request payload
    payload = {
        "text": paper_text,
        "summary_length": summary_length,
        "summary_type": summary_type
    }

    # Set up the API request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {granite_api_key}"
    }

    # Make the API request
    response = requests.post(granite_url, json=payload, headers=headers)

    # Check if the response was successful
    if response.status_code == 200:
        # Extract the summary from the response
        summary = response.json()["summary"]
        return summary
    else:
        # Handle any errors that occurred
        st.error("Error summarizing paper")
        return None

async def main():
    st.title("Research Paper Summarizer")
    st.header("Upload a research paper to generate a summary")

    # Paper input
    uploaded_file = st.file_uploader("Upload a research paper", type=["pdf", "docx", "txt"])

    if uploaded_file:
        # Extract text from the uploaded file
        if uploaded_file.type == "application/pdf":
            pdf_reader = PdfReader(uploaded_file)
            paper_text = "".join([page.extract_text() for page in pdf_reader.pages])
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(uploaded_file)
            paper_text = "".join([para.text for para in doc.paragraphs])
        else:
            paper_text = uploaded_file.read().decode("utf-8")

        # Summary options
        summary_length = st.selectbox("Summary length", ["Short", "Medium", "Long"])
        summary_type = st.selectbox("Summary type", ["Abstract", "Conclusion", "Key points"])

        # Generate summary
        summary = await summarize_paper(paper_text, summary_length, summary_type)

        # Display summary
        st.header("Summary")
        st.write(summary)

if __name__ == "__main__":
    main()

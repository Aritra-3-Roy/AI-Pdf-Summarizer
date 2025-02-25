import streamlit as st
from pdf_processing import extract_text_from_pdf
from summarizer import summarize_text
from report_generator import generate_pdf
st.title("📄 AI-Powered PDF Summarizer")

uploaded_file = st.file_uploader("Upload a PDF:", type='pdf')

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text:",text,height=300)

    if st.button("Summarize"):
        summary = summarize_text(text)
        st.text_area("AI Summary:",summary,height=300)

        pdf_path = generate_pdf(summary)
        st.download_button("Download Report", open(pdf_path, "rb"), file_name="summary_report.pdf")
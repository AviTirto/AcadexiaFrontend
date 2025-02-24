import streamlit as st
from api import get_cloudfareR2, download_file
import asyncio
import base64

st.title("Test Render PDF")

# Initialize the Cloudflare R2 client
r2_client = get_cloudfareR2()

# Specify the file key for the PDF
file_key = "Econ-301/Chapter-2-PPT.pdf"

# Download the file using asyncio
file_obj = asyncio.run(download_file(r2_client, file_key))

file_data = file_obj["file_data"].getvalue()

base64_pdf = base64.b64encode(file_data).decode('utf-8')

page_number = 10

st.markdown(f"""
    <embed src="data:application/pdf;base64,{base64_pdf}#page={page_number}" 
           width="700" height="900" type="application/pdf">
""", unsafe_allow_html=True)

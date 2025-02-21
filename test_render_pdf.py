import streamlit as st
from api import get_cloudfareR2, download_file
from streamlit_pdf_viewer import pdf_viewer
import asyncio
st.title("Test Render PDF")

r2_client = get_cloudfareR2()

file_key = "Econ-301/Chapter-1-PPT.pdf"

file_obj = asyncio.run(download_file(r2_client, file_key))

pdf_viewer(file_obj["file_data"].getvalue())
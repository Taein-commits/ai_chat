# features/document_loader.py
import pandas as pd
from PyPDF2 import PdfReader

def load_document(uploaded_file):
    file_type = uploaded_file.name.split(".")[-1]

    if file_type == "pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    elif file_type == "csv":
        df = pd.read_csv(uploaded_file)
        return df, df.to_string()

    elif file_type == "txt":
        return uploaded_file.read().decode("utf-8")

    return None

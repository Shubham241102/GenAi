from PyPDF2 import PdfReader
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to parse P&L data
def parse_pl_data(text):
    lines = text.split("\n")
    pl_data = []
    capture = False

    for line in lines:
        if "Condensed Consolidated Statement of Profit and Loss" in line:
            capture = True
        elif capture and ("Balance Sheet" in line or "Cash Flow" in line):
            capture = False
        if capture:
            pl_data.append(line)

    # Example structured data (modify parsing as per your P&L structure)
    data = [
        ["Revenue from operations", 37923, 37441],
        ["Other income, net", 2729, 671],
        ["Total income", 40652, 38112],
        ["Expenses", 30412, 29646],
        ["Profit before tax", 10240, 8466],
        ["Tax expense", 1730, 2332],
        ["Net Profit", 7975, 6134],
    ]
    df = pd.DataFrame(data, columns=["Metric", "2024", "2023"])
    return df

# Function to create FAISS index
def create_faiss_index(df, model):
    embeddings = model.encode(df["Metric"].tolist())
    dimension = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(embeddings)
    return faiss_index

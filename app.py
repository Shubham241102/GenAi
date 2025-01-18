import streamlit as st
from utils import extract_text_from_pdf, parse_pl_data, create_faiss_index
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Set Streamlit page title
st.title("Financial QA Bot")
st.write("Upload a financial statement (PDF) and ask queries about the P&L data!")

# Load models
@st.cache_resource
def load_models():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    return model, qa_pipeline

# Query answering function
def answer_query(query, df, model, faiss_index, qa_pipeline):
    query_embedding = model.encode([query])
    distances, indices = faiss_index.search(query_embedding, k=1)
    context = df.iloc[indices[0][0]]["Metric"]
    response = qa_pipeline(question=query, context=context)
    return response["answer"]

# Main Streamlit App
def main():
    # File upload
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file is not None:
        # Extract text from PDF
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
        st.success("PDF text extracted successfully!")

        # Parse P&L data
        with st.spinner("Parsing P&L data..."):
            pl_df = parse_pl_data(text)
        st.success("P&L data parsed successfully!")
        st.write("### Extracted P&L Data")
        st.dataframe(pl_df)

        # Load models
        model, qa_pipeline = load_models()

        # Create FAISS index
        with st.spinner("Creating FAISS index..."):
            faiss_index = create_faiss_index(pl_df, model)
        st.success("FAISS index created successfully!")

        # Query input
        query = st.text_input("Enter your financial query:")
        if query:
            with st.spinner("Generating response..."):
                answer = answer_query(query, pl_df, model, faiss_index, qa_pipeline)
            st.success("Query answered!")
            st.write(f"**Answer:** {answer}")

if __name__ == "__main__":
    main()


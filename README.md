Documentation for Financial QA Bot
________________________________________
Overview
The Financial QA Bot is an interactive web application built using Streamlit. It allows users to upload financial PDF documents containing Profit & Loss (P&L) statements and ask queries about the data. The bot uses a Retrieval-Augmented Generation (RAG) pipeline to answer questions by extracting, structuring, and processing the P&L data.
________________________________________
Features
1.	PDF Upload: Users can upload PDF files containing financial statements.
2.	P&L Data Parsing: Extracts relevant sections of the P&L table and structures them into a tabular format.
3.	RAG Pipeline: 
o	Retrieval: Uses a vector database (FAISS) to retrieve relevant information based on user queries.
o	Answer Generation: Leverages a QA model to generate answers from the retrieved context.
4.	Interactive Interface: Users can view the parsed data, enter queries, and get responses in real time.
________________________________________
Workflow
1. Text Extraction
•	Library: PyPDF2
•	The application reads the uploaded PDF file and extracts text content from it.
2. Data Parsing
•	Identifies and isolates the P&L table from the extracted text.
•	Converts the data into a structured format (e.g., a Pandas DataFrame) with columns: 
o	Metric
o	Values for 2024
o	Values for 2023
3. Embedding and Retrieval
•	Library: Sentence Transformers
•	Generates embeddings for each metric in the P&L table.
•	Stores embeddings in a FAISS vector database for efficient similarity search.
4. Answer Generation
•	Library: Transformers
•	Retrieves the most relevant context using the query embedding.
•	Formats the context with metric names and corresponding values.
•	Uses a question-answering pipeline to generate the answer.
________________________________________
Components
1. app.py
•	The main Streamlit application that: 
o	Manages file uploads.
o	Displays parsed P&L data.
o	Accepts user queries.
o	Calls the RAG pipeline to generate answers.
2. utils.py
•	Contains reusable utility functions: 
o	extract_text_from_pdf: Extracts text from the uploaded PDF.
o	parse_pl_data: Parses and structures P&L data into a DataFrame.
o	create_faiss_index: Creates a FAISS index for storing embeddings.
3. requirements.txt
•	Lists all required libraries and their versions for easy installation.
________________________________________
Setup Instructions
1.	Install Dependencies:
o	Create a virtual environment: 
o	python -m venv myenv
o	source myenv/bin/activate  # For Linux/macOS
o	myenv\Scripts\activate    # For Windows
o	Install the dependencies: 
o	pip install -r requirements.txt
2.	Run the Application:
o	Start the Streamlit app: 
o	streamlit run app.py
3.	Test the Application:
o	Upload a financial PDF containing P&L data.
o	Ask queries such as: 
	"What is the net profit for 2024?"
	"What are the expenses for 2023?"
________________________________________
Example Queries
•	Query: "What is the net profit for 2024?" 
o	Answer: "7975"
•	Query: "What are the total expenses for 2023?" 
o	Answer: "29646"
________________________________________
Libraries Used
1.	Streamlit: For building the interactive web application.
2.	PyPDF2: For extracting text from PDF files.
3.	Pandas: For structuring and processing tabular data.
4.	Sentence Transformers: For generating embeddings.
5.	FAISS: For storing and retrieving vector embeddings.
6.	Transformers: For question-answering using pre-trained models.
________________________________________
Future Improvements
1.	Advanced Parsing: Support more complex or unstructured financial PDFs.
2.	Multi-query Support: Handle compound or multi-part questions.
3.	Deployment: Host the application on a cloud platform like Streamlit Cloud or AWS.
________________________________________
End of Documentation


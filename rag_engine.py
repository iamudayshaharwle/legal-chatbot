import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
#  Load PDFs
folder_path = "data"
pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

all_docs = []
for pdf in pdf_files:
    loader = PyPDFLoader(os.path.join(folder_path, pdf))
    docs = loader.load()
    all_docs.extend(docs)

print(f"Loaded {len(all_docs)} documents from PDFs.")

#  Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
documents = splitter.split_documents(all_docs)

# Create embeddings and store in Chroma
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vectorstore = Chroma.from_documents(documents, embedding=embeddings, persist_directory="Chromadb")


# Save retriever for later use
retriever = vectorstore.as_retriever(search_kwargs={ "k": 5 })

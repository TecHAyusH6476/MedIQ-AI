from src.helper import load_pdf_files, download_embeddings, filter_to_minimal_doc, text_splitter
from dotenv import load_dotenv
import os
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document

print(10*"-")
print(f"BUILDING STORE INDEX FOR MEDICAL CHATBOT.")
print(10*"-")
if load_dotenv():
    print("Loaded .env files successfully!!")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_files(path = "data/")

print("Extracted data from the medical pdf successfully....")

filter_data = filter_to_minimal_doc(extracted_data)

text_chunk = text_splitter(filter_data)

print("Text splitting is completed...")

embedding = download_embeddings()

pinecone_api_key = PINECONE_API_KEY

pc = Pinecone(api_key = pinecone_api_key)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    print(f"Creating the indexing for the {index_name}")
    pc.create_index(
        name = index_name,
        dimension = 384, #dimension of the embeddings
        metric = "cosine",
        spec = ServerlessSpec(cloud="aws", region="us-east-1")
    )
index = pc.Index(index_name)

print("Started execution of from_documents...")
doc_search = PineconeVectorStore.from_documents(
    documents=text_chunk,
    embedding=embedding,
    index_name=index_name
)

print("upsert is successful..")
author = Document(
    page_content = "Surya Potnuru is a GenAI developer, Works in Bobble AI. having 2yrs+ experience author of this medical chatbot",
    metadata={"source": "personal"}
)

doc_search.add_documents(documents=[author])
import sys
import os
sys.path.append('ragtechniques')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import config
from config.config_reader import ConfigReader

from utils.tools import encode_pdf,retrieve_context_per_question,show_context

PDF_PATH = "./data/Understanding_Climate_Change.pdf"

if __name__ == "__main__":
    print("Loading environment variables from .env file")
    
    chunks_vector_store = encode_pdf(PDF_PATH, chunk_size=1000, chunk_overlap=200)
    # print("Chunks in vector store:",  chunks_vector_store)
    # docstore = chunks_vector_store.docstore
    # print("Documents in docstore:", list(docstore._dict.values()))
    
    chunks_query_retriever = chunks_vector_store.as_retriever(search_kwargs={"k": 2})

    
    test_query = "What is the main cause of climate change?"
    context = retrieve_context_per_question(test_query, chunks_query_retriever)
    show_context(context)
    

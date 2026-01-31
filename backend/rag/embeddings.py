from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def get_embedding_model():
    """
    Retruns OpenAI embeddings model
    """
    embeddings = OpenAIEmbeddings(
        model = "text-embedding-3-small",
        api_key = OPENAI_API_KEY
    )
    return embeddings
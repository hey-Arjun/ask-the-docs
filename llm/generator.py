from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_API_KEY = os.environ["OPENAI_API_KEY"]

def generate_answer(prompt: str) -> str:
    """
    Generate final answer from LLM using RAG prompt
    """
    llm = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature = 0,
        api_key = OPEN_API_KEY
    )
    response = llm.invoke(prompt)
    return response.content
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    return llm
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("groq_api_key"), model_name="llama-3.3-70b-versatile")

if __name__ == '__main__':
    response = llm.invoke("What is the capital of india")
    print(response.content)
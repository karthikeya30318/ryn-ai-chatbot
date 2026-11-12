# chat_engine.py

from dotenv import load_dotenv
import os

# Load environment variables from the backend .env file when present.
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFaceHub

# Read provider credentials from environment variables, never hard-code secrets.
google_key = os.getenv("GOOGLE_API_KEY")
huggingface_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Gemini (Google) Chain
def get_gemini_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=1.0
    )
    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=llm, memory=memory, verbose=True)
    return chain

# Hugging Face Chain
def get_huggingface_chain():
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-large",  # You can replace with any supported model
        model_kwargs={"temperature": 0.7, "max_length": 512}
    )
    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=llm, memory=memory, verbose=True)
    return chain

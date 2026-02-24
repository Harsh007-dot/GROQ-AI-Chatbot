import os
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Verify key is loading
api_key = os.getenv("GROQ_API_KEY")
print("Key loaded:", api_key is not None)  # should print True

llm = ChatGroq(model='llama-3.3-70b-versatile')

for reply in llm.stream('Who Is God ?'):
    print(reply.content, end='', flush=True)

print()

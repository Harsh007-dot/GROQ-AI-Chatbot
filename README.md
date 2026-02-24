🏗️ Architecture & Flow
1.	Load environment variables using python-dotenv
2.	Retrieve the GROQ_API_KEY from the environment
3.	Initialize the Groq LLM via LangChain
4.	Send a prompt to the model
5.	Stream the response in real-time
6.	Print the generated tokens progressively
________________________________________
⚙️ Tech Stack
•	Python 3.x
•	LangChain
•	Groq API
•	python-dotenv
•	LLaMA 3.3 70B Versatile Model
________________________________________
📦 Dependencies
•	langchain-groq
•	python-dotenv
Install dependencies:
pip install langchain-groq python-dotenv
________________________________________
🔐 Environment Configuration
Create a .env file in the root directory:
GROQ_API_KEY=your_api_key_here
The script verifies whether the key is loaded correctly before making API calls.
________________________________________
🚀 Key Features
•	✅ Secure API key management using environment variables
•	✅ Real-time token streaming from LLM
•	✅ Minimal and clean implementation
•	✅ Warning suppression for clean console output
•	✅ Easily extensible for chatbot or AI agent systems
________________________________________
🧠 Implementation Details
1️⃣ Environment Loading
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
Loads environment variables securely and verifies key availability.
2️⃣ Model Initialization
llm = ChatGroq(model='llama-3.3-70b-versatile')
Initializes the Groq-hosted LLaMA 3.3 70B versatile model.
3️⃣ Streaming Response
for reply in llm.stream('Who Is God ?'):
    print(reply.content, end='', flush=True)
Uses LangChain's streaming interface to receive and print output incrementally.
This reduces perceived latency and improves user experience for interactive applications.
________________________________________
🔄 Execution Flow
Run the script:
python app.py
Expected Output:
Key loaded: True
<streamed LLM response appears progressively>
________________________________________
📈 Use Cases
•	AI Chatbots
•	Real-time LLM-based CLI tools
•	Research assistants
•	Agentic AI systems
•	Low-latency AI applications


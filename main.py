from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    # google_api_key="YOUR_API_KEY",
)


llm2 = ChatAnthropic(
    model_name="claude-sonnet-4-5-20250929",
    timeout=None,
    stop=None,
)

# llm3 = ChatOpenAI
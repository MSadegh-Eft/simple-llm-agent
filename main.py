from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(
    model_name="claude-sonnet-4-5-20250929",
    timeout=None,
    stop=None,
)
# llm2 = ChatOpenAI


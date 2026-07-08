import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_xai import ChatXAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()


class ReasearchResopnse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]



# print(os.getenv("XAI_API_KEY")) ## checking if the API key is actually loading

llm = ChatXAI(
    model = "grok-4.3"
)


llm2 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    # google_api_key="YOUR_API_KEY",
)


llm3 = ChatAnthropic(
    model_name="claude-sonnet-4-5-20250929",
    timeout=None,
    stop=None,
)

# llm4 = ChatOpenAI


parser = PydanticOutputParser(pydantic_object=ReasearchResopnse) 
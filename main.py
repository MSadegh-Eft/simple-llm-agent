import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_xai import ChatXAI
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()


class ResearchResponse(BaseModel):
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


SYSTEM_PROMPT = """
You are a research assistant that will help generate a research paper.
Use the available tools to gather information before answering -- don't
rely on memory alone. Once you have enough information, call the
save_text_to_file tool to save your findings, then give your final answer.
"""

agent = create_agent(
    model=llm,
    tools=[search_tool, wiki_tool, save_tool],
    system_prompt=SYSTEM_PROMPT,
    response_format=ResearchResponse,
)


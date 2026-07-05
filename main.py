import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_xai import ChatXAI

load_dotenv()

# print(os.getenv("XAI_API_KEY")) ## checking if the API key is actually loading

llm = ChatXAI(
    model = "grok-4.3"
)


# llm2 = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     # google_api_key="YOUR_API_KEY",
# )


# llm3 = ChatAnthropic(
#     model_name="claude-sonnet-4-5-20250929",
#     timeout=None,
#     stop=None,
# )

# # llm4 = ChatOpenAI

response = llm.invoke("what is the meaning of life ? (short answer)")
print(response)
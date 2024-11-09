import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


class LLM:
    def __init__(self, token_limit):
        # Initialize parameters for ChatOpenAI
        self.token_limit = token_limit

    def get_llm(self):
        # Return a ChatOpenAI instance configured with the specified parameters
        return ChatOpenAI(
            openai_api_base=os.getenv("ARIA_BASE_URL"),
            openai_api_key=os.getenv("ARIA_API_KEY"),
            model_name="aria",
        )

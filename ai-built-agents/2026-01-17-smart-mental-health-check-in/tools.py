# tools.py

from langchain_openai import OpenAITool
from prompts import SYSTEM_PROMPT, USER_PROMPT


class AIResponseTool(OpenAITool):
    def __init__(self):
        super().__init__(system_prompt=SYSTEM_PROMPT, user_prompt=USER_PROMPT)

"""
trip_llm.py
───────────
Shared chat-model setup for every lesson that talks to an LLM.

The lessons use LangChain's ChatGoogleGenerativeAI (Google's native Gemini
client). It is used instead of the OpenAI-compatible endpoint because Gemini
tool calls carry a "thought signature" that must be sent back with the tool
result, and only the native client does that. Settings come from .env:

    GEMINI_API_KEY   your Gemini API key
    GEMINI_MODEL     optional, defaults to gemini-flash-lite-latest
                     (gemini-2.5-flash is no longer offered to new API keys)
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-lite-latest")


def make_llm() -> ChatGoogleGenerativeAI:
    # temperature=0 keeps answers as repeatable as possible.
    return ChatGoogleGenerativeAI(
        model=MODEL,
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0,
    )

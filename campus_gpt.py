"""
Very simple CampusGPT RAG logic.

RAG means:
1. Read documents
2. Find useful document lines
3. Send those lines to Gemini
4. Show Gemini's answer
"""

import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_MODEL = "gemini-3.5-flash-lite"


COMMON_WORDS = {
    "what", "is", "the", "a", "an", "of", "for", "to", "in", "on",
    "and", "or", "with", "about", "tell", "me", "please", "can", "you",
    "when", "where", "how", "do", "does", "are", "any", "my", "i",
}


def load_documents(folder_path):
    """
    Read all .txt files from the documents folder.
    """
    # FILL HERE


    pass


def make_chunks(documents):
    """
    Split documents into small searchable lines.
    """
    # FILL HERE


    pass


def clean_text(text):
    """
    Convert text to lowercase and remove simple punctuation.
    """
    # FILL HERE


    pass


def search_documents(question, chunks, limit=3):
    """
    Find the best matching document lines for a question.
    """
    # FILL HERE


    pass


def answer_question(question, chunks):
    """
    Find useful chunks and ask Gemini to answer using only those chunks.
    """
    # FILL HERE


    pass


def ask_gemini(question, results):
    """
    Send the question and retrieved document lines to Gemini.
    """
    # FILL HERE


    pass

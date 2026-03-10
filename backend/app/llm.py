import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"


def generate_answer(query: str, context: list[str]):

    joined_context = "\n\n".join(context)

    prompt = f"""
You are a research assistant.

Answer the question using ONLY the provided context.
If the context is insufficient, say you don't have enough information.

Context:
{joined_context}

Question:
{query}

Answer:
"""

    chat = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return chat.choices[0].message.content
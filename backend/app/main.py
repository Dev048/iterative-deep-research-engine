from fastapi import FastAPI
from app.rag import ask

app = FastAPI()


@app.get("/ask")
def ask_question(query: str):

    result = ask(query)

    return result

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI
from embeddings import search
from rag import generate_answer
from recommend import recommend

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ford Automotive AI Assistant"}

@app.get("/search")
def semantic_search(query: str):
    return {"results": search(query)}

@app.get("/ask")
def ask(query: str):
    return generate_answer(query)

@app.get("/recommend")
def get_recommendation(query: str):
    return {"recommendations": recommend(query)}
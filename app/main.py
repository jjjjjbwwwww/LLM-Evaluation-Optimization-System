
# app/main.py

from fastapi import FastAPI
from app.core.pipeline import EvalPipeline

app = FastAPI()
pipeline = EvalPipeline()

@app.get("/eval")
def evaluate(query: str, answer: str):
    return pipeline.run(query, answer)
from fastapi import FastAPI
from app.services.summarizer import generate_report

app = FastAPI()

# Health Check
@app.get("/")
def home():
    return {"status" : "Agentic Intelligence System Running"}

@app.post("/generate")
def generate(query : str):
    result = generate_report(query)
    return result
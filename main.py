from fastapi import FastAPI

app = FastAPI()

@app.post("/generate-content")
def generate_content(data: dict):
    # Call Google AI API here
    return {"result": "Generated content"}Aimport google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 🔐 Configure Gemini with your API key
genai.configure(api_key="AIzaSyD5l6DZkRHEPrKu5gZOdCb_ZyfmwInCH-A")  # ← Paste your actual key here

class ContentRequest(BaseModel):
    topic: str

@app.post("/generate-content")
def generate_content(data: ContentRequest):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(data.topic)
    return {"result": response.text}

@app.post("/create-worksheet")
def create_worksheet(data: dict):
    # Logic for worksheet creation
    return {"worksheet": "PDF or HTML output"}

@app.post("/query-knowledgebase")
def query_kb(data: dict):
    # Simple Q&A engine
    return {"answer": "Relevant response"}
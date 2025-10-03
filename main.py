from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# 🔐 Configure Gemini with your API key
genai.configure(api_key="AIzaSyD5l6DZkRHEPrKu5gZOdCb_ZyfmwInCH-A")  # ← Replace with your actual key

# 📘 Request model for content generation
class ContentRequest(BaseModel):
    topic: str

# ✨ Gemini-powered content generation with error handling
@app.post("/generate-content")
def generate_content(data: ContentRequest):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(data.topic)
        return {"result": response.text}
    except Exception as e:
        return {"error": str(e)}

# 📝 Placeholder for worksheet creation
@app.post("/create-worksheet")
def create_worksheet(data: dict):
    # Logic for worksheet creation
    return {"worksheet": "PDF or HTML output"}

# 🔍 Placeholder for knowledgebase query
@app.post("/query-knowledgebase")
def query_kb(data: dict):
    # Simple Q&A engine
    return {"answer": "Relevant response"}
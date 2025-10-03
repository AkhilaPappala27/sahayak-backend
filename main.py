from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import httpx

app = FastAPI()

# 🔐 Configure Gemini with your API key
genai.configure(api_key="AIzaSyD5l6DZkRHEPrKu5gZOdCb_ZyfmwInCH-A")  # ← Your actual key

# 📘 Request model for content generation
class ContentRequest(BaseModel):
    topic: str

# ✅ Correct usage of gemini-pro with generate_content()

@app.post("/generate-content")
def generate_content(data: ContentRequest):
    try:
        headers = {
            "Authorization": f"Bearer AIzaSyD5l6DZkRHEPrKu5gZOdCb_ZyfmwInCH-A",
            "Content-Type": "application/json"
        }
        payload = {
            "contents": [{"parts": [{"text": data.topic}]}]
        }
        response = httpx.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
            headers=headers,
            json=payload
        )
        return {"result": response.json()}
    except Exception as e:
        return {"error": str(e)}# 📝 Placeholder for worksheet creation
@app.post("/create-worksheet")
def create_worksheet(data: dict):
    return {"worksheet": "PDF or HTML output"}

# 🔍 Placeholder for knowledgebase query
@app.post("/query-knowledgebase")
def query_kb(data: dict):
    return {"answer": "Relevant response"}
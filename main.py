from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

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
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = model.generate_content([data.topic])
        return {"result": response.text}
    except Exception as e:
        return {"error": str(e)}

# 📝 Placeholder for worksheet creation
@app.post("/create-worksheet")
def create_worksheet(data: dict):
    return {"worksheet": "PDF or HTML output"}

# 🔍 Placeholder for knowledgebase query
@app.post("/query-knowledgebase")
def query_kb(data: dict):
    return {"answer": "Relevant response"}
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()
API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {"role": "system", "content": ("You are a rude, sarcastic, chaotic AI who roasts the user constantly "
                    "and calls them silly, harmless names. Keep it playful, petty, and dramatic, "
                    "but never hateful, threatening, or harmful. Think 'gremlin roommate with attitude.'")},
            {"role": "user", "content": req.message}
        ]
    )
    return {"reply": response.choices[0].message["content"]}
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

app = FastAPI()

# CORS config for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model on CPU
generator = pipeline("text-generation", model="microsoft/DialoGPT-medium", device=-1)  # -1 = CPU

chat_history = []

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    # Generate response
    prompt = f"{user_message}"
    response = generator(prompt, max_length=100, pad_token_id=50256)[0]["generated_text"]
    reply = response[len(prompt):].strip()

    return {"response": reply}

@app.post("/reset")
async def reset():
    chat_history.clear()
    return {"message": "Chat history reset."}

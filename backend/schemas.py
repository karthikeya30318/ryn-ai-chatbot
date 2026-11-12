from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    model_type: str  # "gemini" or "huggingface"

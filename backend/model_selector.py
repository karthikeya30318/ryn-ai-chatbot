from chat_engine import get_gemini_chain, get_huggingface_chain

def select_model_chain(model_type: str):
    if model_type == "gemini":
        return get_gemini_chain()
    elif model_type == "huggingface":
        return get_huggingface_chain()
    else:
        raise ValueError("Invalid model type. Use 'gemini' or 'huggingface'.")

# Ryn — AI Chatbot

Ryn is a conversational AI web application with a React 19 + Vite frontend and a Python FastAPI backend. The repository contains the chatbot interface, API endpoints, and optional LangChain helpers for Google Generative AI and Hugging Face models.

## Repository layout

- backend/ — FastAPI application, model helpers, and Python dependencies
- frontend/ryn-frontend/ — React + Vite client

## Requirements

- Python 3.10+
- Node.js and npm

## Run the backend

1. Open a terminal in the backend directory.
2. Create and activate a Python virtual environment.
3. Install dependencies with: pip install -r requirements.txt
4. Start the API on the port used by the frontend: uvicorn main:app --reload --port 5000

The API is then available at http://localhost:5000. The chat endpoint is POST /chat and the reset endpoint is POST /reset.

## Run the frontend

1. Open another terminal in frontend/ryn-frontend.
2. Install packages with: npm install
3. Start Vite with: npm run dev

Open the local URL printed by Vite (normally http://localhost:5173).

## Environment variables and security

The optional LangChain helpers read provider credentials from backend/.env. Copy backend/.env.example to backend/.env and add your own keys if you use those helpers. Never commit .env files, API keys, access tokens, or other secrets. The .env.example file contains placeholders only.

## Notes

The FastAPI chat endpoint currently uses the Transformers text-generation pipeline configured in backend/main.py. The Google Generative AI and Hugging Face LangChain helpers are defined separately in backend/chat_engine.py and backend/model_selector.py.
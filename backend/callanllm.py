import os
from fastapi import FastAPI, HTTPException, Security, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai


load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

app = FastAPI(title="Chat API")


class ChatIn(BaseModel):
    message: str


messages = []


@app.post("/chat")
def chat(chat_in: ChatIn) -> dict:
    # same 3 moves as your cli , minus input()/print()
    messages.append({"role": "user", "parts": [{"text": chat_in.message}]})

    # 2. send the WHOLE transcript, not just the latest line

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=messages,
    )

    # 3. add the MODEL's reply to the transcript too
    messages.append({"role": "model", "parts": [{"text": response.text}]})
    return {"reply": response.text}

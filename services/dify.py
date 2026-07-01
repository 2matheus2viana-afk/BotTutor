import os
import requests
from dotenv import load_dotenv

load_dotenv()

DIFY_API_KEY = os.getenv("DIFY_API_KEY")

URL = "https://api.dify.ai/v1/chat-messages"


def perguntar_dify(pergunta, usuario):
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},
        "query": pergunta,
        "response_mode": "blocking",
        "conversation_id": "",
        "user": str(usuario)
    }

    resposta = requests.post(URL, headers=headers, json=data)

    if resposta.status_code == 200:
        return resposta.json()["answer"]

    return f"Erro {resposta.status_code}: {resposta.text}"
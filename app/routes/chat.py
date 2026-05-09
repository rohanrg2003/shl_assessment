from fastapi import APIRouter

from app.schemas import ChatRequest
from app.services.conversation_service import (
    process_conversation
)

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    messages = [
        {
            "role": msg.role,
            "content": msg.content
        }
        for msg in request.messages
    ]

    response = process_conversation(messages)

    return response
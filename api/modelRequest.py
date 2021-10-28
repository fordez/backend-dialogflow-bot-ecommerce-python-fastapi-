from typing import Optional, Dict, Any
from pydantic import BaseModel


class Sender(BaseModel):
    id: str


class Recipient(BaseModel):
    id: str


class Message(BaseModel):
    text: str


class Data(BaseModel):
    sender: Sender
    recipient: Recipient
    message: Message


class Payload(BaseModel):
    data: Data


class RequestOriginal(BaseModel):
    source: str
    payload: Payload


class Intent(BaseModel):
    displayName: str


class RequestNlp(BaseModel):
    intent: Intent
    parameters: Dict[str, Any]
    languageCode: str

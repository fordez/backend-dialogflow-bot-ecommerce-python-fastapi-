from typing import Optional, List, Dict, Any, Text
from pydantic import BaseModel


class Payload(BaseModel):
    data: Dict[str, Any]


class RequestOriginal(BaseModel):
    source: str
    payload: Payload


class Intent(BaseModel):
    name: str
    displayName: str


class RequestNlp(BaseModel):
    intent: Intent
    parameters: Dict[str, Any]
    queryText: str
    languageCode: str
    outputContexts: Dict[str, Any]

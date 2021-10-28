from typing import Optional, Dict, Any
from pydantic import BaseModel


class Fulfillment(BaseModel):
    fulfillmentText: Dict[str, Any]

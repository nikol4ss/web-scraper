from typing import List
from datetime import datetime
from pydantic import BaseModel

class PriceEntry(BaseModel):
    product: str
    title: str
    price: float
    timestamp: datetime

class PriceResponse(BaseModel):
    product: str
    average_price: float
    history: List[PriceEntry]

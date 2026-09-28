from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class Order:
    id:str
    customer_id:str
    status:str
    item_id: str
    quantity: int

class OrderAgentResponse(BaseModel):
    order_id: str
    found: bool
    message: str
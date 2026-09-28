from .models import Order
from .mock_data import ORDERS

def get_order(order_id:str) -> Order | None:
    for order in ORDERS:
        if order.id == order_id:
            return order

    return None
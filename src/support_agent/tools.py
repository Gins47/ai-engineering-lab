from agents import function_tool
from .service import get_order

@function_tool
def get_order_tool(order_id:str) -> dict | None:
    """ This tool returns order details for the passed order_id if exists.
        Otherwise, it will return None
    """
    order = get_order(order_id)

    if order is None:
        return None
    
    return {
        "id" : order.id,
        "customer_id" : order.customer_id,
        "item_id": order.item_id,
        "quantity": order.quantity,
        "status": order.status
    } 


if __name__ == "__main__":
    print(type(get_order_tool))
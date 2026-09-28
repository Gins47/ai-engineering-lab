from .models import Order


ORDERS = [
    Order(
        id="123",
        customer_id="CUS12345",
        item_id="IT_12345",
        quantity=4,
        status='COMPLETED'
    ),
        Order(
        id="567",
        customer_id="CUS567",
        item_id="IT_5321",
        quantity=1,
        status='SHIPPED'
    ),
        Order(
        id="467",
        customer_id="CUS658",
        item_id="IT_1178",
        quantity=1,
        status='CANCELLED'
    ),
        Order(
        id="890",
        customer_id="CUS567",
        item_id="IT_5578",
        quantity=1,
        status='REFUNDED'
    ),
        Order(
        id="561",
        customer_id="CUS258",
        item_id="IT_1374",
        quantity=1,
        status='DELIVERED'
    ),
        Order(
        id="982",
        customer_id="CUS8897",
        item_id="IT_65771",
        quantity=1,
        status='CANCELLED'
    )
]
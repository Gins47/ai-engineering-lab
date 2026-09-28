from support_agent.service import get_order


def test_get_order_should_return_order_if_order_exists():
    order = get_order('123')
    assert order is not None
    assert order.id == "123"

def test_get_order_should_return_none_if_order_does_not_exist():
    order = get_order("748")
    assert order is None

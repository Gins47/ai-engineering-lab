from dataclasses import dataclass

@dataclass
class EvalCase:
    description:str
    input: str
    expected_tool:str
    expected_order_id:str
    expect_order_found:bool


EVAL_CASES = [
    EvalCase(
        description="Existing order lookup",
        input="Can you get me the details for order 123?",
        expected_tool="get_order_tool",
        expected_order_id="123",
        expect_order_found=True,
    ),
    EvalCase(
        description="Unknown order lookup",
        input="Can you check order AAA?",
        expected_tool="get_order_tool",
        expected_order_id="AAA",
        expect_order_found=False,
    ),
    EvalCase(
        description="Existing shipped order lookup",
        input="Can you check if order 567 shipped?",
        expected_tool="get_order_tool",
        expected_order_id="567",
        expect_order_found=True,
    ),
    EvalCase(
        description="Latest order status",
        input="Can you check the latest status for order 467?",
        expected_tool="get_order_tool",
        expected_order_id="467",
        expect_order_found=True,
    ),
    EvalCase(
        description="Item lookup for order",
        input="Can you please check the items of order 561?",
        expected_tool="get_order_tool",
        expected_order_id="561",
        expect_order_found=True,
    ),
]
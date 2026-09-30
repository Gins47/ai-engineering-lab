import asyncio

from agents import Runner
from evals.support_agents.extractors import extract_tool_call, extract_tool_call_output
from support_agent.support_agents import order_agent
from evals.support_agents.dataset import EVAL_CASES
from config import get_openai_api_key


# def extract_tool_call(result):
#     for item in result.new_items:
#         if isinstance(item,ToolCallItem):
#             arguments = json.loads(item.raw_item.arguments)
#             return item.raw_item.name , arguments

#     return None,None

def evaluate(case,result):
    tool_name, tool_arguments = extract_tool_call(result)

    tool_output = extract_tool_call_output(result)

    print(f"Tool call output = {tool_output}")

    tool_call_pass = tool_name == case.expected_tool
    tool_argument_pass = tool_arguments is not None and tool_arguments['order_id'] == case.expected_order_id

    order_id_pass = result.final_output.order_id == case.expected_order_id
    found_pass = result.final_output.found == case.expect_order_found

    overall_pass = all([tool_call_pass,tool_argument_pass,order_id_pass,found_pass])

    return {
        "tool":tool_call_pass,
        "arguments":tool_argument_pass,
        "order_id":order_id_pass,
        "order_found":found_pass,
        "overall":overall_pass
    }

async def main():
    get_openai_api_key()

    for case in EVAL_CASES:

        result = await Runner.run(
            order_agent,
            case.input,
        )

        print("\n--- ITEM ---")
        print("Description:", case.description)
        print("Input:", case.input)
        print("Final output:", result.final_output)
        print("Result type:", type(result))
        print(evaluate(case,result))



if __name__ == "__main__":
    asyncio.run(main())


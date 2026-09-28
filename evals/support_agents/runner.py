import asyncio

from agents import Runner

from support_agent.support_agents import order_agent
from evals.support_agents.dataset import EVAL_CASES
from config import get_openai_api_key


async def main():
    get_openai_api_key()
    case = EVAL_CASES[0]

    result = await Runner.run(
        order_agent,
        case.input,
    )

    print("Description:", case.description)
    print("Input:", case.input)
    print("Final output:", result.final_output)
    print("Result type:", type(result))

    for item in result.new_items:
        print("\n--- RUN ITEM ---")
        print("Type: ",type(item))
        print("Item: ",item)



if __name__ == "__main__":
    asyncio.run(main())
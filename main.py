
import asyncio
from config import get_openai_api_key
from agents import Runner
from support_agent.support_agents import order_agent


async def main():
    get_openai_api_key()
    result = await Runner.run(order_agent," Can you please get me the details for order AAA ?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

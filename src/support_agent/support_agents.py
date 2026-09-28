from agents import Agent
from .tools import get_order_tool
from .models import OrderAgentResponse


order_agent = Agent(
    name="Order Agent",
    model="gpt-5-nano",
    instructions="""
    You are an order specialist who helps users understand their order information.

    Rules:
    1. Use the get_order_tool to retrieve order information.
    2. Base your response only on information returned by the tool.
    3. Never invent order information.
    4. If the order does not exist, tell the user that the order could not be found.
    5. Don't mention about any capabilities which the system doesn't support.
    """,
    tools=[get_order_tool],
    output_type=OrderAgentResponse
    )
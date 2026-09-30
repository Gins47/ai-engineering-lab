

import json

from agents import ToolCallItem
from agents import ToolCallOutputItem


def extract_tool_call(result):
    for item in result.new_items:
        if isinstance(item,ToolCallItem):
            arguments = json.loads(item.raw_item.arguments)
            return item.raw_item.name , arguments

    return None,None


def extract_tool_call_output(result):
    for item in result.new_items:
        if isinstance(item,ToolCallOutputItem):
            return item.output
        
    return None
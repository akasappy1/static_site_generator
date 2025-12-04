import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "p" 
    HEADING = "h1"
    CODE = "c"
    QUOTE = "q"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"

def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    final_block_list = []
    for block in block_list:
        new_block = block.rstrip()
        if new_block != "":
            final_block_list.append(new_block)
    return final_block_list

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">") or block.startswith(" >"):
        return BlockType.QUOTE
    elif "\n-" in block:
        return BlockType.UNORDERED_LIST
    elif re.search(r"(\n\d+\.)", block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    


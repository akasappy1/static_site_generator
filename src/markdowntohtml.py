
from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType
from textnode import TextNode, text_node_to_html_node, TextType
from textnodeconversion import text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode

def markdown_to_html_node(markdown):
    initial_blocks = markdown_to_blocks(markdown) #see markdowntoblocks.py
    output_nodes = []
    for block in initial_blocks:
        block_type = block_to_block_type(block) #see markdowntoblocks.py
        block_tag = block_type_to_tag(block, block_type) #see below
        if block_type == BlockType.CODE:
            prefix_and_block = block.split("```")
            stripped_text = prefix_and_block[1]
            if stripped_text.startswith("\n"):
                stripped_text = stripped_text[1:]
            block_text = TextNode(stripped_text, TextType.CODE)
            block_html = text_node_to_html_node(block_text) # see text node.py
            block_html = ParentNode("pre",[block_html])
        elif block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
            block_html = block_to_html_list(block, block_tag)
        elif block_type == BlockType.QUOTE:
            slice_start = block.find(">") + 1
            formatted_block = block[slice_start: ]
            formatted_block = formatted_block.replace("\n >", "")
            formatted_block = formatted_block.replace("\n>", "")
            formatted_block = formatted_block.strip()
            block_children = text_to_children(formatted_block)
            block_html = block_to_parent_node(block_tag, block_children)
        elif block_type == BlockType.HEADING:
            prefix_plus_block = block.split(" ", 1)
            formatted_block = prefix_plus_block[1]
            formatted_block = formatted_block.replace("\n", " ")
            block_children = text_to_children(formatted_block)
            block_html = block_to_parent_node(block_tag, block_children)
        else:
            block = block.replace("\n", " ")
            block_children = text_to_children(block)
            block_html = block_to_parent_node(block_tag, block_children)                                      
        output_nodes.append(block_html)
    html_output = ParentNode("div", output_nodes)
    return html_output

def text_to_children(block_text):
    children = []
    block_children = text_to_textnodes(block_text) # see textnodeconversion.py
    for block in block_children:
        html_node = text_node_to_html_node(block) # see textnode.py
        children.append(html_node)
    return children

    
def block_to_parent_node(block_tag, children):
    if len(children) == 0:
        raise Exception("This block appears to be empty.")
    return ParentNode(block_tag, children)

def block_type_to_tag(block, block_type:BlockType):
    '''Takes a block type and returns an html tag.'''
    if block_type == BlockType.HEADING: 
        return block_to_heading(block)
    elif block_type == BlockType.CODE:
        return "code"
    elif block_type == BlockType.QUOTE:
        return "blockquote"
    elif block_type == BlockType.UNORDERED_LIST:
        return ("ul", "li") # Remember to break up this tuple into the outer parent tag "ul" and inner child tag "li."
    elif block_type == BlockType.ORDERED_LIST:
        return ("ol", "li") # See above comment.
    else:
        return "p" 


def block_to_heading(block):
    pound_counter = 0
    for char in block[0:7]: 
        if char == "#":
            pound_counter += 1
    heading_tag = f"h{pound_counter}"
    return heading_tag

def block_to_html_list(block, block_tags):
        lines = block.splitlines()
        elements = []
        for line in lines:
            if line == "":
                continue   
            if block_tags == ("ul", "li"):
                slice_start = 1
            elif block_tags == ("ol", "li"):
                slice_start = line.find(".") + 1
                if slice_start == 0:
                    raise Exception("Ordered list items must start with a number and period.")
            line = line.lstrip() 
            formatted_line = line[slice_start:]
            formatted_line = formatted_line.lstrip()
            line_children = text_to_children(formatted_line)
            li_node = block_to_parent_node(block_tags[1], line_children)
            elements.append(li_node)
                     
        html_list = ParentNode(block_tags[0], elements)
        return html_list


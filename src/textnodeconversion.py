from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter, split_nodes_images, split_nodes_link

def text_to_textnodes(text):
    first_node = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(first_node, "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    images = split_nodes_images(code)
    final_nodes = split_nodes_link(images)
    return final_nodes
    

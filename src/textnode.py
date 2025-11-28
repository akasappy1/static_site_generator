from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode 

class TextType(Enum):
    TEXT = "p"
    BOLD = "b"
    ITALIC = "i"
    CODE = "c"
    LINK = "a" 
    IMAGE = "img"

class TextNode():

    def __init__(self, content, text_type: TextType, url=None):
        self.text = content
        self.text_type= text_type
        self.url = url
    
    def __eq__(self, text_node):
        if self.text == text_node.text:
            if self.text_type == text_node.text_type:
                if self.url == text_node.url:
                    return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type not in TextType:
        raise Exception("That's not a recognized format.")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

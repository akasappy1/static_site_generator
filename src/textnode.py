from enum import Enum

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE_TEXT = "code text"
    LINK_TEXT = "anchor text + url" 
    IMAGE_TEXT = "alt text + image url"

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
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

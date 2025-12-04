
class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("You Still need to write this")
    
    def props_to_html(self):
        if self.props == {} or self.props == None:
            return ""
        formatted_props = " " + " ".join(fr'{key}="{value}"' for key, value in self.props.items())
        return formatted_props

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, properties={self.props})"
    

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return f"{self.value}"
        elif self.props == None:
            return fr"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return fr"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props={}):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No html tags provided")
        if self.children == None:
            raise ValueError("No children exist. This parent node could've been a leaf node.")
        else:
            children_to_html = [child.to_html() for child in self.children]
            return rf"<{self.tag}>{"".join(str(child) for child in children_to_html)}</{self.tag}>"
        
import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode

case1 = [["This is a text node", TextType.BOLD, None], "TextNode(This is a text node, TextType.BOLD, None)"]
case2 = [["So this is cryptic", TextType.LINK, r"https://www.crosserville.com/"],
         r"TextNode(So this is cryptic, TextType.LINK, https://www.crosserville.com/)"]
case3 = [["No, this is the crypt keeper", TextType.IMAGE, r"https://imagelinkdummy.net"], 
         r"TextNode(No, this is the crypt keeper, TextType.IMAGE, https://imagelinkdummy.net)"]
test_cases = [case1, case2, case3]


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        for case in test_cases:
            node = TextNode(case[0][0], case[0][1], case[0][2])
            node2 = TextNode(case[0][0], case[0][1], case[0][2])
            self.assertEqual(node, node2)
    def test_repr(self):
        for case in test_cases:
            node = TextNode(case[0][0], case[0][1], case[0][2])
            printed_node = node.__repr__()
            expected = case[1]
            self.assertEqual(printed_node, expected)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_img_text(self):
        node = TextNode("Ceci n'est pas un text node", TextType.IMAGE, r"https://upload.wikimedia.org/wikipedia/en/b/b9/MagrittePipe.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://upload.wikimedia.org/wikipedia/en/b/b9/MagrittePipe.jpg", 
                                           "alt": "Ceci n'est pas un text node"})
    def test_ital_text(self):
        node = TextNode("This node makes paleography simple", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This node makes paleography simple")
    
    def test_link_text(self):
        node = TextNode("But this one makes it interpretable", TextType.LINK, 
                        "https://www.nationalarchives.gov.uk/education/resources/palaeography/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "But this one makes it interpretable")
        self.assertEqual(html_node.props, {"href": "https://www.nationalarchives.gov.uk/education/resources/palaeography/"})


if __name__ == "__main__":
    unittest.main()

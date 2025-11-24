# SO MANY TESTS IT GETS ITS OWN FILE
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span><b>grandchild</b></span></div>"
            )
        
    def test_to_html_with_children_p(self):
        child_node = LeafNode("p", "child", {"href": "https://no-creative-css-here.com"})
        parent_node = ParentNode("h1", [child_node])
        self.assertEqual(parent_node.to_html(), '<h1><p href="https://no-creative-css-here.com">child</p></h1>')
    
    def test_to_html_with_children_ps(self):
        child_node = LeafNode("h2", "umea", {"href": "https://no-creative-css-here.com", "lang": "eu"})
        parent_node = ParentNode("h1", [child_node])
        self.assertEqual(parent_node.to_html(), '<h1><h2 href="https://no-creative-css-here.com" lang="eu">umea</h2></h1>')

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError) as ve:
            ParentNode("h2", None).to_html()
        self.assertEqual(str(ve.exception), "No children exist. This parent node could've been a leaf node.")

    def test_to_html_mult_children(self):
        child_node1 = LeafNode("b", "child1", {"lang": "en"})
        child_node2 = LeafNode("i", "figlia2", {"lang": "it"})
        parent_node = ParentNode("p", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), '<p><b lang="en">child1</b><i lang="it">figlia2</i></p>')

    def test_to_html_mult_grands(self):
        grandchild_node1 = LeafNode("p", "nipote", {"lang": "it"})
        grandchild_node2 = LeafNode("i", "grandchild", {"lang": "en"})
        child_node1 = LeafNode("i", "child")
        child_node2 = ParentNode("h2", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("h1", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            '<h1><i>child</i><h2><p lang="it">nipote</p><i lang="en">grandchild</i></h2></h1>' 
                         )

if __name__ == "__main__":
    unittest.main()
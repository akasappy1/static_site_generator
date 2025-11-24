import unittest
import copy

from htmlnode import HTMLNode, LeafNode

html_case1 = [[None, None, None, {"href": r"https://some-css-sheet.com", "link rel": "Some-link-ref"}], 
         r' href="https://some-css-sheet.com" link rel="Some-link-ref"']
html_case2 = [["h1", "Trogdor Burninates", None, {"href": r"https://burninated-fonts-etc.com", "target": "_village"}],
         r' href="https://burninated-fonts-etc.com" target="_village"']
html_case3 = [["h2", "Map of Peasantia Below", None, {"href": r"https://fantasy-version-leaflet.com"}],
         r' href="https://fantasy-version-leaflet.com"']
html_test_cases = [html_case1, html_case2, html_case3]

leaf_case1 = [["h1", "Trogdor Burninates", {"href": r"https://burninated-fonts-etc.com", "target": "_village"}],
         r'<h1 href="https://burninated-fonts-etc.com" target="_village">Trogdor Burninates</h1>']
leaf_case2 = [["h2", "Map of Peasantia Below", {"href": r"https://fantasy-version-leaflet.com"}],
         r'<h2 href="https://fantasy-version-leaflet.com">Map of Peasantia Below</h2>']
leaf_case_3 = [["p", "And then there were many lamentations", {}], "<p>And then there were many lamentations</p>"]
leaf_test_cases = [leaf_case1, leaf_case2, leaf_case_3]

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        for case in html_test_cases:
            node = HTMLNode(tag=case[0][0], value=case[0][1], children=case[0][2], props=case[0][3])
            node_props = node.props_to_html()
            expected_props = case[1]
            self.assertEqual(node_props, expected_props)

    def test_leaf_to_html_p(self):
        for case in leaf_test_cases:
            node_args = case[0]
            node = LeafNode(*node_args)
            node_html = node.to_html()
            expected_html = case[1]
            self.assertEqual(node_html, expected_html)



if __name__ == "__main__":
    unittest.main()
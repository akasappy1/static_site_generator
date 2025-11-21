import unittest

from htmlnode import HTMLNode

case1 = [[None, None, None, {"href": r"https://some-css-sheet.com", "link rel": "Some-link-ref"}], 
         r' href="https://some-css-sheet.com" link rel="Some-link-ref"']
case2 = [["h1", "Trogdor Burninates", None, {"href": r"https://burninated-fonts-etc.com", "target": "_village"}],
         r' href="https://burninated-fonts-etc.com" target="_village"']
case3 = [["h2", "Map of Peasantia Below", None, {"href": r"https://fantasy-version-leaflet.com"}],
         r' href="https://fantasy-version-leaflet.com"']

test_cases = [case1, case2, case3]

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        for case in test_cases:
            node = HTMLNode(*case[0])
            node_props = node.props_to_html()
            expected_props = case[1]
            self.assertEqual(node_props, expected_props)

if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode, TextType

case1 = [["This is a text node", TextType.BOLD, None], "TextNode(This is a text node, bold, None)"]
case2 = [["So this is cryptic", TextType.LINK_TEXT, r"https://www.crosserville.com/"],
         r"TextNode(So this is cryptic, anchor text + url, https://www.crosserville.com/)"]
case3 = [["No, this is the crypt keeper", TextType.IMAGE_TEXT, r"https://imagelinkdummy.net"], 
         r"TextNode(No, this is the crypt keeper, alt text + image url, https://imagelinkdummy.net)"]
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


if __name__ == "__main__":
    unittest.main()

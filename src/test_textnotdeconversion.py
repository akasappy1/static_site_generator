import unittest
from textnode import TextNode, TextType
from textnodeconversion import text_to_textnodes

class TestConversionFunctions(unittest.TestCase):
    def test_with_missing_delimiters(self):
        text = "Text in **bold**, _italic, and a `code block`"
        with self.assertRaises(Exception) as e:
            text_to_textnodes(text)
        self.assertEqual(str(e.exception), "Invalid Markdown syntax: unclosed style tag.")

    def test_with_multiple_images(self):
        text = "No, _this_ isn't rick rolling ![Rick Steves](https://sometravelguy.com) **THIS** is rick rolling ![Rick Astley](https://musicalgod.com)"
        matches = [
            TextNode("No, ", TextType.TEXT),
            TextNode("this", TextType.ITALIC),
            TextNode(" isn't rick rolling ", TextType.TEXT),
            TextNode("Rick Steves", TextType.IMAGE, "https://sometravelguy.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("THIS", TextType.BOLD),
            TextNode(" is rick rolling ", TextType.TEXT),
            TextNode("Rick Astley", TextType.IMAGE, "https://musicalgod.com")
        ]
        self.assertListEqual(matches, text_to_textnodes(text))

if __name__ == "__main__":
    unittest.main()

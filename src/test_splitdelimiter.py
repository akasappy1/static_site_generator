import unittest

from splitdelimiter import split_nodes_delimiter, split_nodes_images, split_nodes_link
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_bold(self):
        bold_node = [TextNode("That's a **bold** claim", TextType.TEXT)]
        b_delimiter = "**"
        b_type = TextType.BOLD
        actual = split_nodes_delimiter(bold_node, b_delimiter, b_type)
        expected = [TextNode("That's a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" claim", TextType.TEXT)]
        self.assertEqual(actual, expected)

    def test_italic(self):
        italic_node = [TextNode("No, it's actually in _italic_ hand", TextType.TEXT)]
        i_delimiter = "_"
        i_type = TextType.ITALIC
        actual = split_nodes_delimiter(italic_node, i_delimiter, i_type)
        expected = [TextNode("No, it's actually in ", TextType.TEXT), 
                    TextNode("italic", TextType.ITALIC), TextNode(" hand", TextType.TEXT)]
        self.assertEqual(actual, expected)

    def test_all_code(self):
        code_node = [TextNode("`Some whole code block here`", TextType.CODE)]
        c_delimiter = "`"
        c_type = TextType.CODE
        actual = split_nodes_delimiter(code_node, c_delimiter, c_type)
        expected = [TextNode("`Some whole code block here`", TextType.CODE)]
        self.assertEqual(actual, expected)

    def test_unclosed_tag(self):
        bad_node = [TextNode("This isn't a **bold word", TextType.TEXT)]
        bad_delimiter = "**"
        type = TextType.BOLD
        with self.assertRaises(Exception) as e:
            split_nodes_delimiter(bad_node, bad_delimiter, type)
        self.assertEqual(str(e.exception), "Invalid Markdown syntax: unclosed style tag.")

    def test_start_tag(self):
        sample_node = [TextNode("_This_ is italic?", TextType.TEXT)]
        sample_sep = "_"
        style = TextType.ITALIC
        actual = split_nodes_delimiter(sample_node, sample_sep, style)
        expected = [TextNode("This", TextType.ITALIC), TextNode(" is italic?", TextType.TEXT)]
        self.assertEqual(actual, expected)

    def test_end_tag(self):
        sample_node = [TextNode("And this is `code`", TextType.TEXT)]
        sample_sep = "`"
        style = TextType.CODE
        actual = split_nodes_delimiter(sample_node, sample_sep, style)
        expected = [TextNode("And this is ", TextType.TEXT), TextNode("code", TextType.CODE)]
        self.assertEqual(actual, expected)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
        ]   ,
            new_nodes,
        )   
        
    def test_split_links(self):
        node = TextNode(
            "This is a [linked listicle](https://dadjokeslist.com)! Sorry, [not sorry](https://regretnothing.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("linked listicle", TextType.LINK, "https://dadjokeslist.com"),
                TextNode("! Sorry, ", TextType.TEXT),
                TextNode("not sorry", TextType.LINK, "https://regretnothing.com")
        ]   ,
            new_nodes,
        )

    def test_starting_link(self):
        node = TextNode(
            "[Click here](https://somelink.com) to reveal your destiny", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Click here", TextType.LINK, "https://somelink.com"),
                TextNode(" to reveal your destiny", TextType.TEXT)
        ]   ,
            new_nodes
        )

    def test_starting_image(self):
        node = TextNode(
            "![Spooky Map](https://badmaps.com) Caption: A spooky map", TextType.TEXT
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("Spooky Map", TextType.IMAGE, "https://badmaps.com"),
                TextNode(" Caption: A spooky map", TextType.TEXT)
        ]   , new_nodes
        )

if __name__ == "__main__":
    unittest.main()
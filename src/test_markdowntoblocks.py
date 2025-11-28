import unittest
from markdowntoblocks import markdown_to_blocks, BlockType, block_to_block_type

class MarkdownBlocksTest(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_w_headers(self):
        md = """
# Here's some text with a big header.

## And a smaller header.



And a paragraph with a `code block`.

And an _italic_ one.
"""
        actual_blocks = markdown_to_blocks(md)
        expected_blocks = ["# Here's some text with a big header.", "## And a smaller header.", 
                           "And a paragraph with a `code block`.", "And an _italic_ one."]
        self.assertListEqual(actual_blocks, expected_blocks)


    def test_3lines_whitespace(self):
        md = """
For some reason **this** paragraph...


And this one are separated by _too many_ new lines.
"""
        expected_blocks = ["For some reason **this** paragraph...", "And this one are separated by _too many_ new lines."]
        actual_blocks = markdown_to_blocks(md)
        self.assertListEqual(actual_blocks, expected_blocks)


    def test_heading_blocktype(self):
        block = "### This is a medium header"
        self.assertEqual(BlockType.HEADING, block_to_block_type(block))

    def test_code_blocktype(self):
        block = "```Here's some sample code.```"
        self.assertEqual(BlockType.CODE, block_to_block_type(block))

    def test_quote_block(self):
        block = """
>Is this the face that launched a thousand ships?
>Sweet Helen make me immortal with a kiss.
"""
        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_unordered_list_block(self):
        block = """
-white beans
-charcoal
-cola
-lentils
"""
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(block))

    def test_ordered_list_block(self):
        block = """
1. Don't talk about Fight Club.
2. Don't talk about Fight Club.
3. If it is your first time at Fight Club, you must fight.
42. Always pack a towel.
"""
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(block))

    def test_paragraph_bloick(self):
        block = "Just some bog-standard ```paragraph``` text."
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

if __name__ == "__main__":
    unittest.main()

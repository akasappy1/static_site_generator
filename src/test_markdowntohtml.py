import unittest

from markdowntohtml import *

class MarkdownHTMLTest(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
    
    def test_quoteblock(self):
        md = """
> Angels and ministers
> of grace defend us.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Angels and ministers of grace defend us.</blockquote></div>"
        )

    def test_headingblock(self):
        md = """
### Shakespeare's _Translators_

## Shakespeare's **Collaborators**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Shakespeare's <i>Translators</i></h3><h2>Shakespeare's <b>Collaborators</b></h2></div>"
        )

    def test_ul(self):
        md = """
What follows is an unordered list:

-**Georgia** peaches
-apples
-nectarines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>What follows is an unordered list:</p><ul><li><b>Georgia</b> peaches</li><li>apples</li><li>nectarines</li></ul></div>"
        )
    def test_ol(self):
        md = """
And here's an ordered list:

1. **Buffalo**
2. _Buffalo_
3.  Buffalo
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            r"<div><p>And here's an ordered list:</p><ol><li><b>Buffalo</b></li><li><i>Buffalo</i></li><li>Buffalo</li></ol></div>"
        )
if __name__ == "__main__":
    unittest.main()


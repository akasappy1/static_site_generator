import unittest
from extraction import extract_markdown_images, extract_markdown_links, extract_title

class ExtractionTests(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
            )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches
        )

    def test_extract_image_not_link(self):
        matches = extract_markdown_images(
            "Ur face ![image](https://rickrollface.com) when you get [rick rolled](https://knowyourmeme.com)"
            )
        self.assertListEqual([("image", "https://rickrollface.com")], matches)

    def test_link_not_image(self):
        matches = extract_markdown_links(
            "Ur face ![image](https://rickrollface.com) when you get [rick rolled](https://knowyourmeme.com)"
        )
        self.assertListEqual([("rick rolled", "https://knowyourmeme.com")], matches)

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "OMG Ur face! ![image](https://rickrollface.com) You got rick rolled! ![image2](https://rickastley.com/png/)"
        )
        self.assertListEqual([("image", "https://rickrollface.com"), ("image2", "https://rickastley.com/png/")], matches)

    def test_link_first(self):
        matches = extract_markdown_links(
            "[Start here](https://firstclickthru.com) and see how you do."
        )
        self.assertListEqual([("Start here", "https://firstclickthru.com")], matches)

    def test_extract_title(self):
        md = """
# Kit Marlowe
## Sexiest death ever?
### Cause all in all, getting stabbed in the eye sound kind of wild.
"""
        actual = extract_title(md)
        self.assertEqual(actual, "Kit Marlowe")

    def test_no_title(self):
        md = """
## No, I like
### Thomas Kyd
"""
        with self.assertRaises(Exception) as e:
            extract_title(md)
        self.assertEqual(str(e.exception), 
                         "No title found in markdown text.")
        
    def test_whitespace_strip(self):
        md = """
#      Ew, Ben Jonson!       
"""
        actual = extract_title(md)
        self.assertEqual(actual, "Ew, Ben Jonson!")
    
if __name__ == "__main__":
    unittest.main()
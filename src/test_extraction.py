import unittest
from extraction import extract_markdown_images, extract_markdown_links

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

    
if __name__ == "__main__":
    unittest.main()
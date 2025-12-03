# from enum import Enum
from textnode import TextType, TextNode
from recursivecopy import recursive_tree_copy
from generate_page import generate_page

def main():
    # sample_node = TextNode("All your graph are belong to us!", 
                           #TextType.BOLD, 
                           #"https://knowyourmeme.com/memes/all-your-base-are-belong-to-us")
    # print(sample_node)
    recursive_tree_copy(
        "/home/aksap/static_site_generator/static",
        "/home/aksap/static_site_generator/public")
    generate_page(
        "/home/aksap/static_site_generator/content/index.md",
        "/home/aksap/static_site_generator/template.html",
        "/home/aksap/static_site_generator/public/index.html"
    )

if __name__ == "__main__":
    main()

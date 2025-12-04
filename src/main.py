# from enum import Enum
import sys

from textnode import TextType, TextNode
from recursivecopy import recursive_tree_copy
from generate_page import generate_page, generate_pages_recursive

def main():
    # sample_node = TextNode("All your graph are belong to us!", 
                           #TextType.BOLD, 
                           #"https://knowyourmeme.com/memes/all-your-base-are-belong-to-us")
    # print(sample_node)
    basepath = sys.argv[0]
    if basepath == None:
        basepath = "/"
    recursive_tree_copy(
        "/home/aksap/static_site_generator/static",
        "/home/aksap/static_site_generator/docs")
    generate_pages_recursive(
        "/home/aksap/static_site_generator/content",
        "/home/aksap/static_site_generator/template.html",
        "/home/aksap/static_site_generator/docs", basepath)
    # generate_page(
    #     "/home/aksap/static_site_generator/content/index.md",
    #     "/home/aksap/static_site_generator/template.html",
    #     "/home/aksap/static_site_generator/public/index.html"
    # )
    # generate_page(
    #     "/home/aksap/static_site_generator/content/blog/glorfindel/index.md",
    #     "/home/aksap/static_site_generator/template.html",
    #     "/home/aksap/static_site_generator/public/blog/glorfindel/index.html"
    # )
    # generate_page(
    #     "/home/aksap/static_site_generator/content/blog/tom/index.md",
    #     "/home/aksap/static_site_generator/template.html",
    #     "/home/aksap/static_site_generator/public/blog/tom/index.html"
    # )
    # generate_page(
    #     "/home/aksap/static_site_generator/content/blog/majesty/index.md",
    #     "/home/aksap/static_site_generator/template.html",
    #     "/home/aksap/static_site_generator/public/blog/majesty/index.html"
    # )
    # generate_page(
    #     "/home/aksap/static_site_generator/content/contact/index.md",
    #     "/home/aksap/static_site_generator/template.html",
    #     "/home/aksap/static_site_generator/public/contact/index.html"
    # )

if __name__ == "__main__":
    main()

# from enum import Enum
from textnode import TextType, TextNode
from recursivecopy import recursive_tree_copy

def main():
    sample_node = TextNode("All your graph are belong to us!", 
                           TextType.BOLD, 
                           "https://knowyourmeme.com/memes/all-your-base-are-belong-to-us")
    print(sample_node)
    recursive_tree_copy(
        "/home/aksap/static_site_generator/static",
        "/home/aksap/static_site_generator/public")

if __name__ == "__main__":
    main()

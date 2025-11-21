from enum import Enum
from textnode import TextType, TextNode

def main():
    sample_node = TextNode("All your graph are belong to us!", TextType.BOLD, "https://knowyourmeme.com/memes/all-your-base-are-belong-to-us")
    print(sample_node)

if __name__ == "__main__":
    main()

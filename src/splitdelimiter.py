from textnode import TextType, TextNode
from extraction import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        if old_node.text_type == TextType.TEXT:
            delimiter_count = -1
            split_node = old_node.text.split(delimiter)
            for text in split_node:
                delimiter_count += 1
                if delimiter_count % 2 == 0:
                    updated_node = TextNode(text, TextType.TEXT)
                    new_nodes.append(updated_node)
                else:
                    updated_node = TextNode(text, text_type)
                    new_nodes.append(updated_node)
            if delimiter_count % 2 != 0:
                raise Exception("Invalid Markdown syntax: unclosed style tag.")
    for node in new_nodes:
        if node.text == "":
            new_nodes.remove(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        anchor_links = extract_markdown_links(text)
        if anchor_links == []:
            new_nodes.append(node)
        else:
            for link_ref in anchor_links:
                anchor = link_ref[0]
                link = link_ref[1]
                sections = text.split(rf"[{anchor}]({link})", 1)
                pretext = sections[0]
                if pretext != "":
                    text_node = TextNode(pretext, TextType.TEXT)
                    new_nodes.append(text_node)
                link_node = TextNode(anchor, TextType.LINK, link)
                new_nodes.append(link_node)
                text = sections[-1]
            if text != "":
                last_text_node = TextNode(text, TextType.TEXT)
                new_nodes.append(last_text_node)
    return new_nodes


def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        image_links = extract_markdown_images(text)
        if image_links == []:
            new_nodes.append(node)
        else:
            for image_ref in image_links:
                alt = image_ref[0]
                image = image_ref[1]
                sections = text.split(f"![{alt}]({image})", 1)
                pretext = sections[0]
                if pretext != "":
                    text_node = TextNode(pretext, TextType.TEXT)
                    new_nodes.append(text_node)
                image_node = TextNode(alt, TextType.IMAGE, image)
                new_nodes.append(image_node)
                text = sections[-1]
            if text != "":
                last_text_node = TextNode(text, TextType.TEXT)
                new_nodes.append(last_text_node)
    return new_nodes

        

    
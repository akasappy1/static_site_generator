from textnode import TextType, TextNode, text_node_to_html_node


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

        

    
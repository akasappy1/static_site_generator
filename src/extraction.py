# Extracts titles, links to images and urls from markdown text.
import re

def extract_markdown_images(text):
    images = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links

def extract_title(text):
    lines = text.splitlines()
    #print(lines)
    for line in lines:
        if line.startswith("# "):
            #print(line)
            title_line = line.split("# ", 1)
            title = title_line[1]
            title = title.strip()
            return title
        
    raise Exception("No title found in markdown text.")
        

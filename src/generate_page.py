import os
from markdowntohtml import markdown_to_html_node
from extraction import extract_title
from htmlnode import ParentNode

def generate_page(from_path, template_path, dest_path):
    """Reads in a markdown file and template to convert it to html."""
    print(f"Generating page from {from_path} to {dest_path}" 
          + f"using {template_path}")
    dest_directory = os.path.dirname(dest_path)
    os.makedirs(dest_directory, exist_ok=True)
    with (open(from_path, "r") as f1, 
          open(template_path, "r+") as f2, 
          open(dest_path, "w+") as f3):
      md_text = f1.read()
      template = f2.read()
      #page_doc = f3.read()
      page_nodes = markdown_to_html_node(md_text)
      page_string = page_nodes.to_html()
      page_title = extract_title(md_text)
      out_html = template.replace(r"{{ Title }}", page_title)
      out_html = out_html.replace(r"{{ Content }}", page_string)
      f3.write(out_html)




     
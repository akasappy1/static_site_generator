import os
from markdowntohtml import markdown_to_html_node
from extraction import extract_title
from htmlnode import ParentNode

def generate_page(from_path, template_path, dest_path, basepath="/"):
    """Reads in a markdown file and template to convert it to html."""
    print(f"Generating page from {from_path} to {dest_path}" 
          + f" using {template_path}")
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
      out_html = out_html.replace(r'href="/', f'href={basepath}')
      out_html = out_html.replace(r'src="/', f'src={basepath}')
      f3.write(out_html)

def generate_pages_recursive(dir_path_content, template_path, 
                             dest_dir_path, basepath="/", base_src_dir = ""):
   """Recursively reads through a directory and generates static html for each
   of the markdown files in it, copying each md file as a separate html file
   in the destination directory."""
   if base_src_dir == "": 
      base_src_dir = dir_path_content
   dir_path = os.path.abspath(dir_path_content) 
   #print(dir_path)
   if os.listdir(dir_path) == []:
      return
   dir_list = os.listdir(dir_path)
   #print(dir_list)
   for item in dir_list:
      item_path = os.path.join(dir_path, item)
      #print(item_path)
      root, ext = os.path.splitext(item_path)
      #print(root)
      #print(ext)
      if ext == ".md":
         src_relpath = os.path.relpath(item_path, base_src_dir)
         print(item_path)
         print(dir_path_content)
         print(src_relpath)
         dest_relpath = str(src_relpath.replace(".md", ".html"))
         print(dest_relpath)
         dest_file_path = os.path.join(dest_dir_path, dest_relpath)
         print(dest_file_path)
         generate_page(item_path, template_path, dest_file_path, basepath)
      else:
         generate_pages_recursive(item_path, template_path, dest_dir_path,
                                  basepath, base_src_dir=base_src_dir)

generate_pages_recursive(
        "/home/aksap/static_site_generator/content",
        "/home/aksap/static_site_generator/template.html",
        "/home/aksap/static_site_generator/docs")

# generate_pages_recursive(
#         "/home/aksap/static_site_generator/content",
#         "/home/aksap/static_site_generator/template.html",
#         "/home/aksap/static_site_generator/public")

     
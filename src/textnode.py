from enum import Enum
from htmlnode import *
import re

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self,text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url 
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            False
        return (self.text == other.text and self.url == other.url and self.text_type == other.text_type)
    
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"

def text_node_to_html_node(text_node):
    match text_node:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("must be a valid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = old_nodes.split(delimiter)
    new_nodes = []
    for node in split_nodes:
        if node == node[0]:
            new_nodes.append(TextNode(node, TextType.NORMAL))
        elif delimiter == "**":
            new_nodes.append(TextNode(node, TextType.BOLD))
        elif delimiter == "*":
            new_nodes.append(TextNode(node, TextType.ITALIC))
        elif delimiter == "`":
            new_nodes.append(TextNode(node, TextType.CODE))
        elif node == node[-1]:
            new_nodes.append(TextNode(node, TextType.NORMAL))
        else: 
            raise Exception("please use a proper delimiter")
        return new_nodes
def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images
def extract_markdown_links(text):
    links = re.findallr("(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)   
    return links
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        parts = node.split("[", 1)
        text = parts[0]
        image = extract_markdown_images(node)
        new_nodes.append(TextNode(text, TextType.NORMAL))
        new_nodes.append(TextNode(image, TextType.IMAGE))
    return new_nodes
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        parts = node.split("[", 1)
        text = parts[0]
        link = extract_markdown_links(node)
        new_nodes.append(TextNode(text, TextType.NORMAL))
        new_nodes.append(TextNode(link, TextType.IMAGE))
    return new_nodes

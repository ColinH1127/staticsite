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
    links = re.findall("(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)   
    return links
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            parts = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))
            new_nodes.append(TextNode(image[0], TextType.IMAGES, image[1]))
            original_text = parts[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            parts = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))
            new_nodes.append(TextNode(link[0], TextType.LINKS, link[1]))
            original_text = parts[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    block = []
    block_list = []
    for line in lines:
        
        stripped_line = line.strip()
        if stripped_line != "":
            block.append(stripped_line)
        if stripped_line == "":
            if block == []:
                continue
            else:
                new_block = "\n".join(block)
                block_list.append(new_block)
                block = []
        if block != []:
            block_list.append(block)
            
    return block_list
        

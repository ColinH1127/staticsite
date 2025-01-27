from enum import Enum

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

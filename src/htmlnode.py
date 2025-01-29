

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("program has not been implemented")
    def props_to_html(self):
        props_string = ""
        for key, value in self.props.items():
            props_string += f" {key}={value}"
        return props_string 
    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value 
        self.props = props
    def to_html(self):
        if self.value == None:
            raise ValueError("All leafnodes must have a value")
        for key, value in self.props.items():
            key = key
            value = value
        if self.tag == None:
            return f"{key}={value} {self.value}" 
        return f"<{self.tag} {key}={value}>{self.value}</{self.tag}>" 
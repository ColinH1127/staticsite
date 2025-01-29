

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("program has not been implemented")
    def props_to_html(self):
        for key, value in self.props.items:
            return f" {key}={value}"
    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"
    

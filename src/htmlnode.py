

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
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props=None)
        self.tag = tag
        self.children = children
        self.props = props
    def to_html(self):
        if self.tag == None:
            raise ValueError("must include a tag")
        if self.children == None:
            raise ValueError("must have a value for children")
        elif self.children == []:
            raise ValueError("must include children")
        result = ""
        if self.props == None:
            result = f"<{self.tag}>"
        else:
            result = f"<{self.tag} {self.props_to_html()}>" 
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result

        
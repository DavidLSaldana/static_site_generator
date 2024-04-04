

class HTMLNode():
    """docstring for HTMLNode."""
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props = self.props
        attr = ""
        for prop in props:
            attr += f' {prop}="{props[prop]}"'
        
        return attr

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    
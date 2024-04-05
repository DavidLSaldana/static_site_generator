from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

        if not self.tag:
            raise ValueError ("Tag shouldn't be None")

        if not self.children:
            raise ValueError ("Children shouldn't be None")

    def to_html(self):
        temp_string = ""
        for i in range(0, len(self.children)):
            temp_string += self.children[i].to_html()
        
        return f"<{self.tag}>{temp_string}</{self.tag}>"

        
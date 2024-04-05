from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    """docstring for TextNode."""
    def __init__(self, text, text_type, url=None):
        super(TextNode, self).__init__()
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        if self.text == text_node.text \
            and self.text_type == text_node.text_type \
            and self.url == text_node.url:
                return True
        else:
            return False
            
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.link, "alt": text_node.text})
    raise ValueError (f"Invalid text type: {text_node.text_type}")
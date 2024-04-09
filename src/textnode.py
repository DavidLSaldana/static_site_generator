import re
from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

code_delimit = '`'
bold_delimit = '**'
italic_delimit = '*'

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #takes list of old nodes, a delimiter, and a text type
    #returns a new list of nodes where any "text" type are
    #potentially split based on syntax
    new_text_type = ""
    new_list_nodes = []
    if delimiter == code_delimit:
        new_text_type = text_type_code
    if delimiter == italic_delimit:
        new_text_type = text_type_italic
    if delimiter == bold_delimit:
        new_text_type = text_type_bold
    
    temp_func = lambda delimit: delimit.text.split(delimiter)

    for node in old_nodes:
        
        if not node.text_type == text_type_text:
            new_list_nodes.append(node)
        else:
            working_node = temp_func(node)
            working_node_length = len(working_node)
            if working_node_length % 2 == 0:
                raise Exception("Invalid Markdown Syntax")

            for w_node in range(0, len(working_node)):
                if w_node %2 == 1:
                    new_list_nodes.append(TextNode(working_node[w_node],new_text_type,None))
                else:
                    new_list_nodes.append(TextNode(working_node[w_node],text_type_text,None))

    return new_list_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    matches = extract_markdown_images(old_nodes.text)
    if not matches:
        return old_nodes
    new_list_nodes = []
    splits = len(matches)
    if splits >= 1:
        working_node = old_nodes.text.split(f"![{matches[0][0]}]({matches[0][1]})", 1)

        #node gets text broken into 3 parts here:
        #part 1 - before first match, will be a text_type
        #part 2 - the match, will be image type
        #part 3 - everything after the first match, text_type for the recursive call

        #part 1
        if working_node[0] == "":
            pass
        else:
            new_list_nodes.append(TextNode(working_node[0],text_type_text, None))

        #part 2 - the actual image
        new_list_nodes.append(TextNode(matches[0][0],text_type_image,matches[0][1]))

        #part 3 - peaking ahead to see if there is anything there
        if not working_node[1]:
            return new_list_nodes
        else:
            temp_node = TextNode(working_node[1],text_type_text)
            new_list_nodes.append(split_nodes_image(temp_node))

    return new_list_nodes


def split_nodes_link(old_nodes):
    matches = extract_markdown_links(old_nodes.text)
    if not matches:
        return old_nodes
    new_list_nodes = []
    splits = len(matches)
    if splits >= 1:
        working_node = old_nodes.text.split(f"[{matches[0][0]}]({matches[0][1]})", 1)

        #same as split nodes image, node gets text broken into 3 parts here:
        #part 1 - before first match, will be a text_type
        #part 2 - the match, will be link type
        #part 3 - everything after the first match, text_type for the recursive call

        #part 1
        if working_node[0] == "":
            pass
        else:
            new_list_nodes.append(TextNode(working_node[0],text_type_text, None))

        #part 2 - the actual link
        new_list_nodes.append(TextNode(matches[0][0],text_type_link,matches[0][1]))

        #part 3 - peaking ahead to see if there is anything for a recursive call
        if not working_node[1]:
            return new_list_nodes
        else:
            temp_node = TextNode(working_node[1],text_type_text)
            new_list_nodes.append(split_nodes_image(temp_node))

    return new_list_nodes

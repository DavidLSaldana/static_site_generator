from htmlnode import HTMLNode
from enum import Enum

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

class Block_State(Enum):
    NO_STATE = 0
    QUOTE = 1
    U_LIST = 2
    O_LIST = 3

def markdown_to_blocks(markdown):
    split_contents = markdown.split("\n\n")
    result = []
    #will use filter to remove empty lines
    #will use strip to remove spaces from start of lines
    rem_whitespace = lambda content: content.strip()
    is_empty = lambda text: text != ""
    result = list(map(rem_whitespace, split_contents))
    result = list(filter(is_empty, result))
    return result

def block_to_block_type(markdown_block):
    md_block_length = len(markdown_block)
    if md_block_length == 0:
        return None
    
    if "# " in markdown_block[0:7]:
        return block_type_heading
    if "```" in markdown_block[0:3] and "```" in markdown_block[ len(markdown_block)-3 : ]:
        return block_type_code
    split_block = markdown_block.split("\n")
    state = Block_State.NO_STATE
    if split_block[0][0] == ">":
        state = Block_State.QUOTE
    if split_block[0][0] == "*" or split_block[0][0] == "-":
        state = Block_State.U_LIST
    if split_block[0][0:2] == "1.":
        state = Block_State.O_LIST
    for line in range(0, len(split_block)):
        if state == Block_State.QUOTE:
            if split_block[line][0] == ">":
                pass
            else:
                state = Block_State.NO_STATE
        if state == Block_State.U_LIST:
            if split_block[line][0] == "*" or split_block[line][0] == "-":
                pass
            else:
                state = Block_State.NO_STATE
        if state == Block_State.O_LIST:
            if f"{line+1}. " in split_block[line][0:4]:
                pass
            else:
                state = Block_State.NO_STATE
        if state == Block_State.NO_STATE:
            return block_type_paragraph
        elif state == Block_State.QUOTE:
            return block_type_quote
        elif state == Block_State.U_LIST:
            return block_type_unordered_list
        elif state == Block_State.O_LIST:
            return block_type_ordered_list

    return block_type_paragraph

    
def paragraph_block_to_htmlnode(block, block_type):
    
    return new_node

def heading_block_to_htmlnode():
    pass

def code_block_to_htmlnode():
    pass

def quote_block_to_htmlnode():
    pass

def unordered_list_block_to_htmlnode():
    pass

def ordered_list_block_to_htmlnode():
    pass
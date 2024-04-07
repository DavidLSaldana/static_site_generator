import unittest

from textnode import *
#from textnode import TextNode
#from textnode import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        print(f"node: {node1}")
        print(f"node2: {node2}")
        self.assertEqual(node1, node2)

        node3 = TextNode("This is a node", "bold")
        node4 = TextNode("This is a text node", "Italic", "www.mysite.com")
        node5 = TextNode("This is text with a `code block` word", text_type_text)
        node6 = TextNode("This is text with an error `code block word", text_type_text)
        new_nodes = split_nodes_delimiter([node5], "`", text_type_code)
        print(f"No Error: new_nodes {new_nodes}")
        #new_nodes = split_nodes_delimiter([node6], "`", text_type_code)
        #print(f"With Error: new_nodes {new_nodes}")

        node7 = TextNode("This is text with a `code block` and an *Italic Word* and a **Bold Word**", text_type_text)
        new_nodes = split_nodes_delimiter([node7], "**", text_type_code)
        print(f"No Error: new_nodes {new_nodes}")

        #print(f"node3: {node3}")
        #print(f"node4: {node4}")
        #self.assertEqual(node3, node4)

        #print(f"node5: {node5}")
        #print(f"node4: {node4}")
        #self.assertEqual(node5, node4)
        
if __name__ == "__main__":
    unittest.main()
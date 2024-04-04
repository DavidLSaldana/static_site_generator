import unittest

from htmlnode import HTMLNode

class HTMLNodeTest(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p", "This is a parg",None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a parg",None, {"href": "https://www.google.com"})
        node3 = HTMLNode("a", "This is a parg",None, {"href": "https://www.google.com"})
        print(f"node1: {node1}")
        print(f"node2: {node2}")
        print(f"node3: {node3}")

        print(node1.props_to_html())


        
if __name__ == "__main__":
    unittest.main()
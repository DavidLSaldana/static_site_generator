import unittest

from leafnode import LeafNode


class HTMLNodeTest(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "This is a parg", {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode("p", "This is a parg", {"href": "https://www.google.com"})
        print(f"node1: {node1}")
        print(f"node2: {node2}")

        print(f"node1.to_html(): {node1.to_html()}")
        print(f"node2.to_html(): {node2.to_html()}")


        
if __name__ == "__main__":
    unittest.main()
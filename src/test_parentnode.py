import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class HTMLNodeTest(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
        "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )

        print(node.to_html())

    #need many more unit tests!

        
if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        print(f"node: {node1}")
        print(f"node2: {node2}")
        self.assertEqual(node1, node2)

        node3 = TextNode("This is a node", "bold")
        node4 = TextNode("This is a text node", "Italic")
        node5 = TextNode("This is a text node", "Italic", "www.mysite.com")

        #print(f"node3: {node3}")
        #print(f"node4: {node4}")
        #self.assertEqual(node3, node4)

        #print(f"node5: {node5}")
        #print(f"node4: {node4}")
        #self.assertEqual(node5, node4)
        
if __name__ == "__main__":
    unittest.main()
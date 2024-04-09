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
        test_extract_text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ..png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        print(extract_markdown_images(test_extract_text))
        print(type(extract_markdown_images(test_extract_text)))

        test_extract_images_text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        print(extract_markdown_links(test_extract_images_text))

        node8 = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
        new_nodes = split_nodes_image(node8)
        print(f"new_nodes: {new_nodes}")

        node9 = TextNode("![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)", text_type_text,)
        new_nodes2 = split_nodes_image(node9)
        print(f"new_nodes2: {new_nodes2}")

        node10 = TextNode("no matches here", text_type_text,)
        new_nodes3 = split_nodes_image(node10)
        print(f"new_nodes3: {new_nodes3}")

        node11 = TextNode(
    "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
        new_nodes11 = split_nodes_link(node11)
        print(f"new_nodes11: {new_nodes11}")

        node12 = TextNode("[link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)", text_type_text,)
        new_nodes12 = split_nodes_link(node12)
        print(f"new_nodes12: {new_nodes12}")

        node13 = TextNode("no matches here", text_type_text,)
        new_nodes13 = split_nodes_image(node10)
        print(f"new_nodes13: {new_nodes13}")




        
if __name__ == "__main__":
    unittest.main()
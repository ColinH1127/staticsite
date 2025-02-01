import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_notequal(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTML:
    def test_eq(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        expected_result = "<b>This is not a text node</b>"
        self.assertEqual(node.text_node_to_html_node,)



if __name__ == "__main__":
    unittest.main()
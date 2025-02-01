import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode 

class TestHTMLNode(unittest.TestCase):
    def test_default_initialization(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
    def test_values(self):
        node = HTMLNode("a", None, None, {"href" : "www.google.com" })
        self.assertDictEqual(node.props, {"href" : "www.google.com"})
        self.assertEqual(node.tag, "a")
    def test_repr(self):
        node = HTMLNode("h1", "This is a Test")
        expected_output = "h1 This is a Test None None"
        self.assertEqual(repr(node), expected_output)
    def test_props(self):
        node = HTMLNode(None, None, None, {"href": "www.google.com", "src": "www.yahoo.com"})
        expected_output = " href=www.google.com src=www.yahoo.com"
        self.assertEqual(node.props_to_html(), expected_output)
class TestLeafNode(unittest.TestCase):
    def test_values(self):
        node = LeafNode("h1", "This is a test", {"href": "www.google.com"})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "This is a test")
        self.assertEqual(node.props, {"href": "www.google.com"})
    def test_to_html(self):
        node = LeafNode("h1", "This is a test", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), "<h1 href=www.google.com>This is a test</h1>")
    def test_error(self):
        node = LeafNode("h1", None, {"href": "www.google.com"})
        self.assertRaises(ValueError)
class TestParentNode(unittest.TestCase):
    def test_values(self):
        node = ParentNode("h1", [LeafNode("p", "this is a test", {"href": "www.google.com"})], {"href": "www.google.com"})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.props, {"href": "www.google.com"})
    

if __name__ == "__main__":
    unittest.main()
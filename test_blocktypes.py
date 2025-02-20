import unittest
from blocktypes import BlockTypes, block_to_block_type

block1 = "# Heading 1"
block2 = "```python\nprint('Hello, world!')\n```"
block3 = "> Another line in the blockquote."
block4 = "1. First item"
block5 = "- Item 2"
block6 = "This is a paragraph"

class TestBlockTypes(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(block_to_block_type(block1), BlockTypes.HEADING)
        self.assertEqual(block_to_block_type(block2), BlockTypes.CODE)
        self.assertEqual(block_to_block_type(block3), BlockTypes.QUOTE)
        self.assertEqual(block_to_block_type(block4), BlockTypes.ORDERED_LIST)
        self.assertEqual(block_to_block_type(block5), BlockTypes.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(block6), BlockTypes.PARAGRAPH)
        
if __name__ == "__main__":
    unittest.main()
import unittest

from blocktype import *


class TestBlockType(unittest.TestCase):
    def test_eq(self):
        
        test_markdown_to_blocks = markdown_to_blocks("""This is **bolded** paragraph

>This is another paragraph with *italic* text and 'code' here
>This is the same paragraph on a new line

#### List with items, but unordered

* This is a list
* with items


```This is a code block```

## ordered list coming up

1. This is an ordered list
2. a
3. b
4. yea
5. this is the end

# Over
""")
        print (f"Testing Markdown to Blocks: {test_markdown_to_blocks}")

        print(("\n").join(list(map(block_to_block_type, test_markdown_to_blocks))))

        
if __name__ == "__main__":
    unittest.main()
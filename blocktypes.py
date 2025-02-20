from enum import Enum

class BlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code" 
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(text):
    match text.splitlines()[0]:
        case line if line.startswith("#"):
            return BlockTypes.HEADING
        case line if line.startswith("```"):
            return BlockTypes.CODE
        case line if line.startswith(">"):
            return BlockTypes.QUOTE
        case line if line.startswith("* ") or line.startswith("- "):
            return BlockTypes.UNORDERED_LIST
        case line if line[0].isdigit() and ". " in line:
            return BlockTypes.ORDERED_LIST
        case _:
            return BlockTypes.PARAGRAPH
        

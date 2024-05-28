from enum import Enum

class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4

def convert_format(content, from_format, to_format):
    if from_format == DocFormat.MD and to_format == DocFormat.HTML:
        return "<h1>"+content.lstrip("# ")+"</h1>"
    if from_format == DocFormat.TXT and to_format == DocFormat.PDF:
        return f"[PDF] {content} [PDF]"
    if from_format == DocFormat.HTML and to_format == DocFormat.MD:
        return content.replace("<h1>","# ").replace("</h1>","")
    raise Exception("Invalid type")
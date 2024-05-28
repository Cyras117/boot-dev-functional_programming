doc_type_pdf = "pdf"
doc_type_txt = "txt"
doc_type_docx = "docx"
doc_type_md = "md"
doc_type_html = "html"


def conversion_type(doc_type):
    match doc_type:
        case "pdf" :
            return doc_type_html
        case "txt":
            return doc_type_pdf
        case "docx":
            return doc_type_md
        case "md":
            return doc_type_pdf
        case "html":
            return doc_type_txt
        case _:
            raise Exception("Unknown document type")

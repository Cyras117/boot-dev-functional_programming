def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = []
        for arg in args:
            converted_args.append(convert_md_to_txt(arg))
        for key, value in kwargs.items():
            kwargs[key] = convert_md_to_txt(value)
        return func(*converted_args, **kwargs)
    return wrapper

def convert_md_to_txt(doc):
    return "\n".join(map( lambda line: line.lstrip("# "),doc.split("\n")))

# Don't edit below this line


@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""
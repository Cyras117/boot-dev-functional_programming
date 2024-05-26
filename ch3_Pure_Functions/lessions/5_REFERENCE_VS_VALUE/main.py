def add_format(default_formats, new_format):
    old_formats = default_formats.copy()
    old_formats[new_format] = True
    return old_formats


def remove_format(default_formats, old_format):
    old_formats = default_formats.copy()
    old_formats[old_format] = False
    return old_formats

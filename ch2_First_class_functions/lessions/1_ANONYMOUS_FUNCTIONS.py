def categorize_file(filename):
    filetypes={".txt":"Text",
                ".docx":"Document",
                ".py":"Code"}
    get_category = lambda extension: filetypes.get(extension,"Unknown")
    return get_category(filename[filename.rfind(".") :])

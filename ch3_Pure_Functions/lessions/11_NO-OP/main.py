def markdown_to_text(doc_content):
    lines = doc_content.split("\n")
    new_lines = map(lambda line: remove_asterisks_from_words(line.lstrip("#")), lines)
    return "\n".join(new_lines)


def remove_asterisks_from_words(line):
    words = line.split()

    def clean_word(word):
        return word.strip("*") if len(word) > 1 else word

    cleaned_words = filter(lambda word: len(word) > 0, map(clean_word, words))
    return " ".join(cleaned_words)

import functools

def accumulate(doc, sentence):
    return doc + ". " + sentence

def accumulate_first_sentences(sentences, n):
    if len(sentences) <= 0 or n <= 0:
        return ""
    return functools.reduce(accumulate,sentences[:n]) + "."
    

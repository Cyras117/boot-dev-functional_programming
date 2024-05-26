def word_count_memo(document, memos):
    memos_updated = memos.copy()
    if not document in memos_updated:
        memos_updated[document] = word_count(document)
    return memos_updated[document],memos_updated
# Don't edit below this line

def word_count(document):
    count = len(document.split())
    return count
def count_nested_levels(nested_documents, target_document_id, level=1):
        for node in nested_documents:
            if node == target_document_id:
                    return level
            r_level = count_nested_levels(nested_documents[node],target_document_id,level+1)
            if r_level != -1:
                return r_level
        return -1
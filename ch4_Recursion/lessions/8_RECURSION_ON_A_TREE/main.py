def list_files(current_node, current_path=""):
    file_list = []
    for node in current_node:
        node_vals = current_node[node]
        if node_vals is None:
            file_list.append(current_path + "/" + node)
        else:
            file_list.extend(list_files(node_vals, current_path + "/" + node))
    return file_list
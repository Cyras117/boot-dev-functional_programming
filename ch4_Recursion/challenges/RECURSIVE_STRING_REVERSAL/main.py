def reverse_string(s):
    new_string = ""
    if len(s) <= 1:
        return s
    new_string += reverse_string(s[1:])
    return  new_string + s[0]
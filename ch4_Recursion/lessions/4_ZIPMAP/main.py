def zipmap(keys, values):
    res = {}
    if len(keys) <= 0 or len(values) <= 0:
        return {}
    res[keys[0]]= values[0]
    res.update(zipmap(keys[1:],values[1:]))
    return res

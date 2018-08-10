def itranslate(dic, string):
    str = ""
    result = []
    key = list(string.split())
    for k in key:
        if k in dic.keys():
            result.append(dic[k])
        else:
            raise KeyError('Missing word')
    return " ".join(result)

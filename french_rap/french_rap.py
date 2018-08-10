def french_rap(csv):
    try:
        list_read = {}
        f = open(csv, 'r')
        str = f.read()
        arr = str.splitlines()
        for x in arr:
            divide = x.index(',')
            list_read.setdefault(x[divide + 1:], []).append(x[:divide])
        f.close()
        return list_read
    except FileNotFoundError:
        raise FileNotFoundError('File does not exist')

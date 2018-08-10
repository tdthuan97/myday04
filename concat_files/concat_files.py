import os


def concat_files(*arg):
    size = len(arg)
    result = ""
    for i in range(size):
        if os.path.isfile("./" + arg[i]):
            f = open(arg[i], 'r')
            result += f.read()
            f.close()
    f = open('concatenated_files', 'a')
    f.write(result)
    f.close()

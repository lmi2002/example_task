def strTuple(st):
    list = []
    for i in range(len(st)):
        list.append(ord(st[i]))
    return tuple(list)

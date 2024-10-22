def prov(s, strr):
    n = 0
    for i in strr:
        if s == i:
            n += 1
    return n

print(prov('e', 'eeeee'))

strr = 'qwertyuiorrr'

print(strr.count('r'))
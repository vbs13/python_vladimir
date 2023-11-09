def shifr(txt, key):
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    res = ''
    for i in txt:
        res += alf[(alf.index(i) + key) % len(alf)]
    return res


print(shifr('абвя', 1))

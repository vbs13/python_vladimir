import itertools

x = itertools.permutations('МИТРОФАН', 6)

k = 0
for i in x:
    a = ''.join(i)
    if (a.count('М') + a.count('Т') + a.count('Р') + a.count('Ф') + a.count('Н')) > (a.count('И') + a.count('А') + a.count('О')):
        if ('АИ' not in a) and ('АО' not in a) and ('ОИ' not in a) and ('ОА' not in a) and ('ИА' not in a) and ('ИО' not in a):
            k += 1
print(k)
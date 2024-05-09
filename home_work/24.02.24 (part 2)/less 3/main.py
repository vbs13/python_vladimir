# n = input('Введите строку: ')
# n = n.title()
# print('Результат:', n)


def big(s: str):
    a = s[0]
    s = a.upper() + s[1:]
    return s

mas = []
n = input('Введите строчку: ')
n = n.split()
for i in n:
    mas.append(big(i))
print(' '.join(mas))
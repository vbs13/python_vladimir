n = input('Доступное меню: ')
x = n.split(';')
for i in range(len(x) - 1):
    print(x[i], end=', ')
print(x[-1])
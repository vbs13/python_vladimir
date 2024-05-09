n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', k, '-й человек')
mas = [x for x in range(1, n + 1)]
x = 0

for i in range(n - 1):
    kill = (k) % len(mas)
    y = mas[kill]
    print('\nТекущий круг людей: ', mas)
    print('Начало счёта с номера: ', mas.index(y))
    print('Выбывает человек под номером: ', y)
    x = y
    del mas[mas.index(y)]


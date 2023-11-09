summ = int(input('Стоимость: '))
s = int(input('Площадь: '))

if (s >= 100 and summ <= 10000000) or (s >= 80 and summ <= 7000000):
    print('Подходит')
else:
    print('Не подходит')

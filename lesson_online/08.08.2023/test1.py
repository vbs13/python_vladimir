s = int(input('Введите количество опыта: '))
print('Ваш уровень: ', end='')
if s < 1000:
    print(1)
elif s >= 1000 and s < 2500:
    print(2)
elif s >= 2500 and s < 5000:
    print(3)
elif s >= 5000:
    print(4)
import random

a = random.randint(1, 1000)
print(a)
b = 0
kol = 0

while a != b:
    kol += 1
    b = int(input('Введите ваше число: '))
    if a == b:
        print('Вы угадали!', kol, 'попыток')
    elif a > b:
        print('Ваше число меньше')
    else:
        print('Ваше число больше')

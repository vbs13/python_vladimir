import random

num = random.randint(1, 1000)
kol = 0
while True:
    n = int(input('Угадайте число: '))
    kol += 1
    if n == num:
        print('Вы угадали')
        print(kol)
        break
    elif n > num:
        print('Ваше число больше загаданного')
    elif n < num:
        print('Ваше число меньше загаданного')

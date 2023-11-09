# главное меню
def menu():
    print('Привет, дорогой друг!')
    print('1 - угадай число, 2 - кнб, 0 - выход')
    game = int(input('Выбери игру: '))
    if game == 0:
        return 0
    elif game == 1:
        number()
    elif game == 2:
        rps()

# угадай число
def number():
    print('Игра угадай число')
    n = 100
    while True:
        num = int(input('Введите число: '))
        if num != n:
            continue
        else:
            print('Вы угадали!')
            menu()

# кнб
def rps():
    print('Игра кнб')


menu()

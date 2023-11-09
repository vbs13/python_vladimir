money = int(input('Деньги: '))

if money < 0:
    print('Доход не может быть отрицательным')
elif money < 10000:
    print(money * 0.13)
elif money >= 10000 and money < 50000:
    print(money * 0.20)
elif money >= 50000:
    print(money * 0.30)

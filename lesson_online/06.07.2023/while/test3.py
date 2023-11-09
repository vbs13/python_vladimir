money = int(input('Стартовая сумма: '))

while money < 10000:
    kub = int(input())
    if kub != 3:
        money += 500
        print('Вы выиграли 500 рублей')
    else:
        money = 0
        print('Вы проиграли всё')
        break

print('Игра окончена')
print('Итого осталось:', money, 'рублей')
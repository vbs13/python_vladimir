bread = 50

money = int(input('Сколько у вас денег? '))
if money >= bread:
    print('Вы купили хлеб')
    print('У вас осталось: ', money - bread, 'денег')
else:
    print('Денег не хватило')
    print('Вам не хватило: ', bread - money, 'денег')
print('Хорошего дня')

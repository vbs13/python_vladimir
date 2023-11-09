dolz = input('Имя должника: ')
summ = int(input('Сумма долга: '))

print(dolz + ', ваша задолжность составляет',  summ, 'рублей')

while summ > 0:
    summ1 = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    if summ1 >= summ:
        summ = 0
        print('Отлично ' + dolz + '! Вы погасили долг. Спасибо!')
    else:
        print('Маловато ' + dolz + '. Давайте еще раз.')
        continue

    
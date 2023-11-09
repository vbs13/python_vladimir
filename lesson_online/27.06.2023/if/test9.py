money = int(input('Деньги: '))
cheese = 60
ice_cream = 20
if money < cheese:
    print('Денег маловато')
else:
    print('На сыр денег хватило')
    if money - cheese >= ice_cream:
        print('И на мороженое тоже!')
    else:
        print('Денег маловато')

    
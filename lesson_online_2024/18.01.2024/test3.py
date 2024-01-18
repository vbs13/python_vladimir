text = input('Введите текст: ')
alf_rus = 'уеыаоэяию'
mas = [x for x in text if x in alf_rus]
print(mas)
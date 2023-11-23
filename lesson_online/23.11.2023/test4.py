s = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')

mas1 = [2 * x for x in s]
print(mas1)
mas2 = [x + symbol for x in mas1]
print(mas2)
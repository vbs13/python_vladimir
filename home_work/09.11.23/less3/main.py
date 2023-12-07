s = input('Введите слово: ')
for i in s:
    if len(s) % 2 == 0:
        if s[i] == s[i::-1]:
            print('палиндром')
        else:
            print('не палиндром')
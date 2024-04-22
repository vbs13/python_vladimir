def col(s):
    k = 0
    for i in s:
        if i.isdigit == True:
            k += 1
    if k >= 3:
        return True
    else:
        return False


n = input('Придумайте пароль: ')

while True:
    if len(n) < 8:
        if n.islower() == True:
            if col(n) == False:
                print('Пароль ненадёжный. Попробуйте ещё раз.')
                n = input('Придумайте пароль: ')
                continue
            else:
                print('Это надёжный пароль!')
                break
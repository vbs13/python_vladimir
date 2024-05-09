def num(s: str):
    k = 0
    for i in s:
        if i.isdigit():
            k += 1
    return k

passw = input('Придумайте пароль: ')
flag = False
while flag != True:
    if len(passw) >= 8:
        if passw.islower() == False:
            if num(passw) >= 3:
                print('Это надежный пароль!')
                flag = True
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        passw = input('Придумайте пароль: ')
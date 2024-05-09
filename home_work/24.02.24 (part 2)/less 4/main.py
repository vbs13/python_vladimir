def num(s: str):
    k = 0
    for i in s:
        if i.isdigit():
            k += 1
    return k

def up(s: str):
    for i in s:
        if i.isupper():
            return True
    return False

passw = input('Придумайте пароль: ')
while True:
    if len(passw) < 8 or num(passw) < 3 or up(passw) == False:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        passw = input('Придумайте пароль: ')
    else:
        print('Это надёжный пароль!')
        break
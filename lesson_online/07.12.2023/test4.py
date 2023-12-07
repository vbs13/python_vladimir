def count_digits(s):
    res = 0
    for i in s:
        res += int(i)
    return str(res)


def obrabotka(s):
    mas = s.split()
    res = ''
    for i in range(len(mas)):
        if mas[i].isdigit() == True:
            mas[i] = count_digits(mas[i])
    res = ' '.join(mas)
    return res


s = input()
print(obrabotka(s))
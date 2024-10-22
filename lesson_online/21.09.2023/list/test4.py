def atob(mas):
    a = max(mas)
    n = mas.index(a)
    b = min(mas)
    n1 = mas.index(b)
    mas[n] = b
    mas[n1] = a
    return mas


mas = [3, 7, -5, 2, 9]
print(atob(mas))
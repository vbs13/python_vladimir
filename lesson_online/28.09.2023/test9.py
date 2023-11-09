a = [12, 43, 124, 5, 77]
b = int(input())

if b in a:
    a.remove(b)
    print(a)
else:
    print('Такого нет')
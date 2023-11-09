def nod(n1):
    mas = [1, n1]
    for i in range(2, n1//2 + 1):
        if n1 % i == 0:
            mas.append(i)
    return sorted(mas)


def nod1(n1, n2):
    a = min(n1, n2)
    for i in range(a, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
             return i
    

print(nod(12))
print(nod1(11, 7))
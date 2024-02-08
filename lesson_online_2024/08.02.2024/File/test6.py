mas = [int(x) for x in open('C:/Users/Владимир/Downloads/17 (1).txt')]

k = []
for i in range(len(mas) - 1):
    for j in range(i + 1, len(mas)):
        if abs(mas[i] - mas[j]) % 2 == 0 and (mas[i] % 31 == 0 or mas[j] % 31 == 0):
            k.append(mas[i] + mas[j])


print(len(k))
print(max(k))
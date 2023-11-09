import random


mas = []
for i in range(100):
    mas.append(random.randint(-1000, 1000))
print(mas)

maxx = 0
k = 0
for i in range(len(mas) - 1):
    if (mas[i] - mas[i + 1]) % 2 == 0 and (mas[i] % 19 == 0 or mas[i + 1] % 19 == 0):
        k += 1
        if maxx < mas[i] + mas[i + 1]:
            maxx = mas[i] + mas[i + 1]
print(k, maxx)

import random

kol = 5
mas = []

for _ in range(kol):
    mas.append(random.randint(0, 9))
print(mas)

mas1 = []
for i in range(0, kol, 2):
    mas1.append(mas[i])
print(mas1)
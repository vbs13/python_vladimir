import random

mas = []
for i in range(10):
    mas.append(random.randint(0, 10))
print(mas)


for i in range(0, 10, 2):
    print(mas[i], mas[i + 1])
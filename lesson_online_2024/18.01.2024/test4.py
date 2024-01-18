import random


mas = [round((random.random() + random.randint(1, 2)), 2) for x in range(10)]
mas1 = [round((random.random() + random.randint(1, 2)), 2) for x in range(10)]
mas2 = [1 if mas[x] > mas1[x] else 2 for x in range(len(mas))]
print(mas)
print(mas1)
print(mas2)
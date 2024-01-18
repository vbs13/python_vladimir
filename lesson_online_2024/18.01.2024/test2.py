import random


mas = [random.randint(0, 10) for i in range(10)]
print(mas)

mas2 = [x for x in mas if x % 2 == 0]
print(mas2)

mas3 = [x if x % 2 != 0 else 0 for x in mas]
print(mas3)
import random


mas = [random.randint(-9, 10) for x in range(10)]
mas1 = [x if x > 0 else 0 for x in mas]
print(mas)
print(mas1)
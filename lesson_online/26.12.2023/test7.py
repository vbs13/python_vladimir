import random


mas = [random.randint(50, 81) for x in range(10)]
mas1 = [random.randint(30, 61) for x in range(10)]
mas2 = ['Погиб' if mas[x] + mas1[x] > 100 else 'Выжил' for x in range(10)]
print(mas)
print(mas1)
print(mas2)
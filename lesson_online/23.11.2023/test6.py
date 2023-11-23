import random

mas1 = [random.randint(50, 80) for x in range(10)]
mas2 = [random.randint(30, 70) for x in range(10)]

print('Урон первого отряда:', mas1)
print('Урон втрого отряда:', mas2)

mas3 = ['Погиб' if mas1[x] + mas2[x] > 100 else 'Выжил' for x in range(10)]
print(mas3)
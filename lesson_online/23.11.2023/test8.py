import random
mas = [random.randint(-50, 50) for x in range(5)]
print(mas)
mas1 = mas[0::]
for i in range(len(mas1)):
    if mas1[i] < 0:
        mas1[i] = 0
print('Мы потеряли', sum(mas) - sum(mas1))
print(mas, mas1)
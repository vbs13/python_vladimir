import random


mas1 = [round((random.random() + random.randint(5, 10)), 2) for x in range(20)]
print(mas1)
mas2 = [round((random.random() + random.randint(5, 10)), 2) for x in range(20)]
print(mas2)
mas_res = [mas1[x] if mas1[x] > mas2[x] else mas2[x] for x in range(len(mas1))]

print(mas_res)
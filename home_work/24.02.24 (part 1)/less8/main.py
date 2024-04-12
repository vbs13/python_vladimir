mas = [int(x) for x in open('17_4414.txt')]
mas1 = []

for i in range(len(mas) - 1):
    for j in range(i + 1, len(mas)):
        if (abs(mas[i] - mas[j]) % 36 == 0) and ((mas[i] % 13 == 0) or (mas[j] % 13 == 0) or ((mas[i] % 13 == 0) and (mas[j] % 13 == 0))):
            mas1.append(abs(mas[i] - mas[j]))
print(len(mas1), max(mas1))
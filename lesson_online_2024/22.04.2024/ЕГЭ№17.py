mas = [int(x) for x in open('C:/Users/Владимир/Downloads/17_15333.txt')]
maxx = max([x for x in mas if x % 19 == 0])
mas1 = []

for i in range(len(mas) - 1):
    if mas[i] > maxx or mas[i + 1] > maxx:
        mas1.append(mas[i] + mas[i + 1])
print(len(mas1), max(mas1))
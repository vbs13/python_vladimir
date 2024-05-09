mas = [int(x) for x in open('17_16328.txt')]
minn = min([x for x in mas if x % 19 == 0])
# res = []
maxx_sum = 0
k = 0

for i in range(len(mas) - 1):
    if mas[i] % minn == 0 or mas[i + 1] % minn == 0:
        # res.append(mas[i] + mas[i + 1])
        k += 1
        maxx_sum = max(maxx_sum, mas[i] + mas[i + 1])
print(k, maxx_sum)
mas = sorted([int(i) for i in open('28141.txt')])
usb = 6147

k = 0
summ = 0
for i in range(len(mas) - 1):
    if summ + mas[i] <= usb:
        summ += mas[i]
        k += 1

delta = usb - summ + mas[k - 1]
res = max([i for i in mas if i <= delta])

print(k, res)
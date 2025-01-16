mas = sorted([int(x) for x in open('28138.txt')])
usb = 6589

k = 0
summ = 0
for i in range(len(mas) - 1):
    if summ + mas[i] <= 6589:
        summ += mas[i]
        k += 1

delta = usb - summ + mas[k - 1]
x = max([i for i in mas if i <= delta])

print(k, x)
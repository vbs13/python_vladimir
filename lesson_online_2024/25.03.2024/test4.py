a = [100, 12, 24, 34, 21, 15, 43, 3, 5, 7, 10, 13]
usb = a.pop(0)

mas = []
a.sort()
for i in a:
    if sum(mas) + i <= 100:
        mas.append(i)
print(len(mas))
delta = usb - sum(mas) + max(mas)
print(max([x for x in a if x <= delta]))

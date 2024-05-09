usb = 9979
mas = [int(x) for x in open('26_2944.txt')]
mas.sort()
res = []

for i in mas:
    if sum(res) + i <= usb:
        res.append(i)
print(len(res))
a = usb - sum(res) + res[-1]
maxx = max([x for x in mas if x <= a])
print(maxx)


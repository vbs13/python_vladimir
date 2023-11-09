summ = int(input())
proc = int(input())
rez = int(input())
a = 0

while (summ < rez) or (summ != rez):
    summ = (summ * proc + summ) // 100
    if summ == rez:
        print(a)
        break
    else:
        a += 1

print(a)


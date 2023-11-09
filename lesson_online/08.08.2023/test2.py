num = int(input())
summ = 0

if num == 0:
    summ = 1

while num > 0:
    num //= 10
    summ += 1
print(summ)
num = int(input())
summ = 1

while num != 0:
    if num % 10 == 0:
        break
    summ *= num % 10
    num //= 10

print(summ)

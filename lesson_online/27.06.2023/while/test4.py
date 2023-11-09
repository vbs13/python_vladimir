num = int(input())
summ = 0

while num != 0:
    if num % 6 == 0 and num % 10 == 4:
        summ += num
    num = int(input())
print(summ)

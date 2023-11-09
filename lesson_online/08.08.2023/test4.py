summ = int(input())
num = 0
num1 = 0

for i in range(1, summ + 1):
    num1 += i

for i in range(1, summ):
    a = int(input())
    num += a

print(num1 - num)
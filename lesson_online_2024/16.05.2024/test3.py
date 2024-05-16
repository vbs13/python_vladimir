def p(n):
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def chet(n):
    res = ''
    while n != 0:
        res = str(n % 4) + res
        n //= 4
    return res


n = int(input())
mas = [int(input()) for x in range(n)]
k = 0
m = 0

for i in range(len(mas) - 1):
    if p(mas[i]) + p(mas[i + 1]) == 1:
        if chet(mas[i])[-2:] == '11' or chet(mas[i + 1])[-2:] == '11':
            k += 1
            m = max(mas[i] + mas[i + 1], m)

print(k, m)
def xin10(s, x):
    a = 0
    b = len(s) - 1
    for i in s:
        a += int(i) * x**b
        b -= 1
    return a


print(xin10('324', 5))
print(int('324', 5))
def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a

#for i in range(2, 6):
#    fact(i)

r = fact(5)
print(r)
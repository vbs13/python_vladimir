N = [1, 2, 3, 4, 5]
K = int(input('Сдвиг: '))
a = 0
for i in range(K):
    a = N[-1]
    N.pop(-1)
    N.insert(0, a)
print(N)
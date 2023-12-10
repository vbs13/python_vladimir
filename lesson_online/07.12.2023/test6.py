m = input()
n = input()
A = m.split()
B = n.split()
print(A)
print(B)

C = []

for i in range(len(B) + 1):
    for j in range(len(A) + 1):
        if A[j] == B[i]:
            C.append(i)
print(C)

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = []
#
# for i in A:
#     if i not in C and i not in B:
#         C.append(i)
#
# for i in B:
#     if i not in C and i not in A:
#         C.append(i)
#
# C.sort()
# if C != []:
#     print(*C)
# else:
#     print('NO')


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = set(A + B)
print(C)
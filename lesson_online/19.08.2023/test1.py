a = input()
flag = True

for i in range(len(a)//2):
    if a[i] != a[(i+1) * -1]:
        flag = False
        break

print(flag)
col = int(input())
chet = 0
flag = False

for i in range(col):
    a = int(input())
    if a >= 10:
        if int(str(a)[-2]) % 2 == 0:
            flag = True
            chet += a

if flag == False:
    print('NO')
else:
    print(chet)

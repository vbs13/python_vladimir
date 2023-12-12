n = int(input())
obm = 0
res = []

for i in range(n):
    col_xolod = []
    xolod = input().split()
    col_xolod.append(xolod[0])
    znah = xolod[1].split('*')
    col_xolod.append(znah)
    res.append(col_xolod)

for i in range(len(res)):
    obm += int(res[i][1][0]) * int(res[i][1][1]) * int(res[i][1][2])
sr = obm / n

new_res = []

for i in res:
     if int(i[1][0]) * int(i[1][1]) * int(i[1][2]) > sr:
         new_res.append(i)

for j in range(len(new_res) - 1):
    for i in range(len(new_res) - 1):
        if new_res[i][0] > new_res[i + 1][0]:
            new_res[i], new_res[i + 1] = new_res[i + 1], new_res[i]
        elif new_res[i][0] == new_res[i + 1][0]:
            if new_res[i][1][0] < new_res[i + 1][1][0]:
                new_res[i], new_res[i + 1] = new_res[i + 1], new_res[i]
            elif new_res[i][1][0] == new_res[i + 1][1][0]:
                if new_res[i][1][1] > new_res[i + 1][1][1]:
                    new_res[i], new_res[i + 1] = new_res[i + 1], new_res[i]
                elif new_res[i][1][1] == new_res[i + 1][1][1]:
                    if new_res[i][1][2] > new_res[i + 1][1][2]:
                        new_res[i], new_res[i + 1] = new_res[i + 1], new_res[i]

for i in new_res:
    i[1] = '*'.join(i[1])
    print(*i)



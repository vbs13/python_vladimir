import csv

with open('C:/Users/Владимир/Downloads/9.20_14661.csv') as f:
    data = csv.reader(f, delimiter=';')
    l = 0
    for elem in data:
        q = list(map(int, elem))
        flag_chet = []
        flag_nechet = []
        for i in q:
            if i % 2 == 0:
                flag_chet.append(i)
            else:
                flag_nechet.append(i)
        if len(flag_chet) >= 1 and len(flag_nechet) >= 1:
            if len(flag_chet) % 2 == 0 and len(flag_nechet) % 2 != 0:
                if max(flag_chet) % 4 == 0:
                    l += 1
print(l)


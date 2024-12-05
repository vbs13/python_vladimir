def dell(x, y):
    return x % y == 0


# for a in range(1, 1001):
#     flag = True
#     for x in range(1, 1001):
#         if (((not(dell(x, 7))) and dell(x, 13)) <= (x > a - 40)) == 0:
#             flag = False
#             break
#     if flag:
#         print(a)


for a in range(1, 1001):
    for x in range(1, 1001):
        if ((not(dell(x, 7)) and dell(x, 13)) <= (x > a - 40)) == 0:
            break
        else:
            continue
    else:
        print(a)

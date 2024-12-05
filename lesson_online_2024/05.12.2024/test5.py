for a in range(1, 1001):
    for x in range(1, 151):
        for y in range(1, 151):
            if (((x <= 9) <= ((x * x) <= a)) and (((y * y) <= a) <= (y <= 9))) == 0:
                break
        else:
            continue
        break
    else:
        print(a)


# for a in range(0, 1000):
#     flag = True
#     for x in range(0, 501):
#         for y in range(0, 501):
#             if (((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6))) == 0:
#                 flag = False
#                 break
#     if flag == True:
#         print(a)
for a in range(1000):
    for x in range(1, 301):
        for y in range(1, 301):
            if ((x - y >= 39) or (y <= x) or (y >= a - 20)) == 0:
                break
        else:
            continue
        break
    else:
        print(a)


# for a in range(1000):
#     flag = True
#     for x in range(1, 301):
#         for y in range(1, 301):
#             if ((x - y >= 39) or (y <= x) or (y >= a - 20)) == 0:
#                 flag = False
#                 break
#     if flag:
#         print(a)

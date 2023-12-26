# mas = []
# for i in range(0, 10):
#     if i % 2 != 0:
#         mas.append(i)
#     else:
#         mas.append(0)
# print(mas)


mas = [i if i % 2 != 0 else 0 for i in range(0, 10)]
print(mas)
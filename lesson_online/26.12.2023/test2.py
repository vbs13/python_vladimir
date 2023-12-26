# mas = []
# for i in range(0, 10):
#     if i % 3 == 0:
#         mas.append(i)
# print(mas)


mas = [i for i in range(0, 10) if i % 3 == 0]
print(mas)
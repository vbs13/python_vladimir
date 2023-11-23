mas = [21, 4, 876, 44, 1, 9]

# m = []
# for i in mas:
#     if i % 2 == 0:
#         m.append(i)
# print(m)

m = [x for x in mas if x % 2 == 0]
print(m)
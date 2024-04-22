# f = open('C:/Users/Владимир/Desktop/test9.csv')
# mas = []
#
# for i in f:
#     mas.append(list(map(int, i.strip().split(';'))))
# print(mas)


mas = [list(map(int, x.strip().split(';'))) for x in open('C:/Users/Владимир/Desktop/test9.csv')]
print(mas)
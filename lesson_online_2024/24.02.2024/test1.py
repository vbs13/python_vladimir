# f = open('1.txt', 'r')
# d = f.readlines()
# mas = []
#
# for i in d:
#     mas.append(int(i))
# print(mas)


# f = open('1.txt', 'r')
# d = f.readlines()
# mas = [int(x) for x in d]
# print(mas)


# mas = []
# for i in open('1.txt', 'r'):
#     mas.append(int(i))
# print(mas)


# mas = [int(x) for x in open('1.txt', 'r')]
# print(mas)


d = open('1.txt', 'r').readlines()
a = list(map(int, d))
print(a)
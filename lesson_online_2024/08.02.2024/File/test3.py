# f = open('C:/Users/Владимир/Desktop/araa.txt')
# t = f.readlines()
# a = list(map(int, t))
# print(a)

# mas = []
# f = open('C:/Users/Владимир/Desktop/araa.txt')
# for i in f:
#     mas.append(int(i))
# print(mas)

mas = [int(x) for x in open('C:/Users/Владимир/Desktop/araa.txt')]
print(mas)
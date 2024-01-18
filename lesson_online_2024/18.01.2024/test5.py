a = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

b = [[0 for y in range(3)] for x in range(4)]
print(b)

c = [[[0 for z in range(2)] for y in range(3)] for x in range(4)]
print(c)

d = [[x + y for y in range(3)] for x in range(1, 13, 3)]
print(d)
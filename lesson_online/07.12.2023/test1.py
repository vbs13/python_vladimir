import math

def point(x, y):
    if x in range(-1, 2) and y in range(-6, 0):
        return 'y'
    elif x in range(-4, 5) and y == -8:
        return 'g'
    elif x in range(-4, 5) and y == 0:
        return 'b'
    elif y > 0 and math.sqrt(x**2 + y**2) < 5:
        return 'r'
    elif y > 0 and math.sqrt(x**2 + y**2) == 5:
        return 'b'
    elif y == -7 and x in range(-4, 5):
        return 'b'
    elif y in range(-9, -6) and x == -5:
        return 'b'
    elif y in range(-9, -6) and x == 5:
        return 'b'
    elif y in range(-7, 1) and x == -2:
        return 'b'
    elif y in range(-7, 1) and x == 2:
        return 'b'
    elif y == -9 and x in range(-4, 5):
        return 'b'
    else:
        return 'w'


x = int(input())
y = int(input())

print(point(x, y))

# for y in range(5, -10, -1):
#     for x in range(-5, 6):
#         if x == 0 and y == 0:
#             print('*', end=' ')
#         else:
#             print(x, end=' ')
#     print()

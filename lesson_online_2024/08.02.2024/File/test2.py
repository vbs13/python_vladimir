import random

f = open('C:/Users/Владимир/Desktop/araa.txt', 'w')
# f.write('hello\n')
for _ in range(10):
    f.write(str(random.randint(-10, 10)) + '\n')
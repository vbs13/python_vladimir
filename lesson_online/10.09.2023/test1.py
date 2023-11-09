a = 1
print(type(a))

b = 'asd'
print(type(b))

c = 'vhvjs'
if isinstance(c, int):
    print('Целое число')
elif isinstance(c, float):
    print('Вещественное')
else:
    print('Не число')

print(5 > 2)
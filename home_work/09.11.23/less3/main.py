# a = s[:len(s)//2]
# if len(s) % 2 != 0:
#     b = s[:len(s) // 2:-1]
# else:
#     b = s[:len(s) // 2 - 1:-1]
# print(a, b)
# if a == b:
#     print('палиндром')
# else:
#     print('не палиндром')


def palindrom(st):
    for i in range(len(st)//2):
        if st[i] != st[-(i + 1)]:
            return False
    return True


s = input('Введите слово: ')
if palindrom(s):
    print('палиндром')
else:
    print('не палиндром')
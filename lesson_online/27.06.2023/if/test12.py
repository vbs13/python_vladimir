time = int(input())

if (time >= 0 and time <= 7) or (time >= 22 and time <= 23) or (time == 14) or \
        (time >= 10 and time < 12) or (time >= 18 and time < 20):
    print('Нельзя')
else:
    print('Можно')
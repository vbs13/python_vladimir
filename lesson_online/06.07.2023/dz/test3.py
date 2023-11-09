good = 0
bad = 0

while True:
    ans = int(input('Введите число: '))
    if ans == 0:
        break
    elif ans > 0:
        good += 1
    elif ans < 0:
        bad += 1

print(good, bad)
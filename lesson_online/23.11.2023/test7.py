mas1 = [x for x in range(10) if x % 2 == 0]
mas2 = [x if x % 2 == 0 else '*' for x in range(10)]
print(mas2)
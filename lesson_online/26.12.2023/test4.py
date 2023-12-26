left, right = map(int, input().split())

mas2 = [x**2 for x in range(left, right + 1)]
mas3 = [x**3 for x in range(left, right + 1)]

print(mas2, mas3)
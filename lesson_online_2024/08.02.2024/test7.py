def grasshoper(n, treasure):
    if n == 0:
        return 0
    elif n == 1:
        return treasure[0]
    else:
        return max(grasshoper(n - 1, treasure), grasshoper(n - 2, treasure)) + treasure[n - 1]


print(grasshoper(6, [1, 2, 3, 6, 2, 1]))
print(grasshoper(7, [-1, -2, 4, 18, -2, 0, 9]))
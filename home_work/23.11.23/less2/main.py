n = int(input())

mas = [1 if x % 2 == 0 else x % 5 for x in range(n)]
print(mas)
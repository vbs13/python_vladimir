def prost(n: int) -> bool:
    for d in range(2, (n // 2) + 1):
        if n % d == 0:
            return False
    return True

for i in range(10, 16):
    print(i, prost(i))



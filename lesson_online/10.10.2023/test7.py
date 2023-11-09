def prost(n: int) -> bool:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


for i in range(245690, 245756):
    if prost(i) == True:
        print(i - 245690 + 1, i)
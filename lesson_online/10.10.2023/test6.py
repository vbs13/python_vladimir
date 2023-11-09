def sost(n: int) -> list:
    mas = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            mas.append(i)
    return mas

for i in range(174457, 174506):
    if len(sost(i)) == 2:
        print(i, sorted(sost(i)))
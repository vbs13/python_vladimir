def delete(n: int) -> list:
    mas = [1, n]
    for d in range(2, (n // 2) + 1):
        if n % d == 0:
            mas.append(d)
    return sorted(mas)


print(delete(12))
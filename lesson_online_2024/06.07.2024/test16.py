f = {1: 1}
for n in range(2, 2025):
    f[n] = (n - 1) * f[n - 1]
print(((f[2024] // 7) - f[2023]) / f[2022])
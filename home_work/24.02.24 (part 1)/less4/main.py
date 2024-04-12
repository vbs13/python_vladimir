mas = []
for x in range(19):
    if (int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)) % 18 == 0:
       mas.append(x)
minn = min(mas)
x = minn
res = (int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)) // 18
print(res)
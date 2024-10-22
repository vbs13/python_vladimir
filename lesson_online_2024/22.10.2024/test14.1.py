x = '0123456789abcdefghi'

for i in x:
    if (int(f'98897{i}21', 19) + int(f'2{i}923', 19)) % 18 == 0:
        print(i, (int(f'98897{i}21', 19) + int(f'2{i}923', 19)) // 18)
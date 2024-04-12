for i in range(20):
    for j in range(20):
        for z in range(20):
            s = '0' + i * '1' + j * '2' + z * '3' + '0'
            while '00' not in s:
                s = s.replace('01', '220', 1)
                s = s.replace('02', '1013', 1)
                s = s.replace('03', '120', 1)
            if s.count('1') == 13 and s.count('2') == 18:
                print(i + j + z + 2)

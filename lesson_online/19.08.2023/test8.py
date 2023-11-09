for i in range(5):
    for j in range(5):
        if i % 2 != 0:
            print('0', end='\t')
        else:
            print('*', end='\t')
    print()
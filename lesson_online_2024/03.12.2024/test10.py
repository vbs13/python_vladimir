import itertools

chet = '2468'
nechet = '1357'
x = itertools.product(chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet)

k = 0
for i in x:
    a = ''.join(i)
    if (a.count('1') <= 4) and (a.count('2') <= 4) and (a.count('3') <= 4) and (a.count('4') <= 4) and (a.count('5') <= 4)\
        and (a.count('6') <= 4) and (a.count('7') <= 4) and (a.count('8') <= 4):
        k += 1


x = itertools.product(nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet)

for i in x:
    a = ''.join(i)
    if (a.count('1') <= 4) and (a.count('2') <= 4) and (a.count('3') <= 4) and (a.count('4') <= 4) and (a.count('5') <= 4)\
        and (a.count('6') <= 4) and (a.count('7') <= 4) and (a.count('8') <= 4):
        k += 1
print(k)




n = input('Введите строку: ')
x = n.split(' ')
alf = 'QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
alf1 = 'qwertyuiopasdfghjklzxcvbnйцукенгшщзхъфывапролджэячсмитьбю'
k = 0

for i in x:
    if i[0] in alf1:
        k = alf1.index(i[0])
        i = i.replace(i[0], alf[k], 1)
print(x)
print(k)
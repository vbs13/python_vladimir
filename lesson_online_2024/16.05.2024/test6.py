name = input()
f = open(name)
mas = [x.strip() for x in f]
print(mas)
mas2 = [x for x in mas if 'C' in x]
print(mas2)
mas3 = []

for elem in mas2:
    m = []
    s = ''
    for c in elem:
        if 'XVII' not in s + c:
            s += c

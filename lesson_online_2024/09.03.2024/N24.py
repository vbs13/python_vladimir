f = open('24_12111.txt')
s = f.read()

s = s.replace('HPY', '*').replace('NYN', '*')
s = s.replace('H', ' ').replace('P', ' ').replace('N', ' ').replace('Y', ' ')

a = s.split()
maxx = 0

for i in range(len(a)):
    if maxx < len(a[i]):
        maxx = len(a[i])
print(maxx)
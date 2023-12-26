st = 'привет'

st2 = [x + x for x in st]
st3 = [x + '!' for x in st2]
# st2 = [st[x] * 2 for x in range(len(st))]
# st3 = [st2[x] + '!' for x in range(len(st2))]
print(st2, st3)
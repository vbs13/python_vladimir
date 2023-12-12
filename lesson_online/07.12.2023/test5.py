m, n = input().split()
s = list(map(int, input().split()))

s.append(0)
mas = []
mas1 = []
st = []

for i in range(1, len(s)):
    if s[i] - 1 != s[i - 1]:
        if len(mas1) == 0:
            mas.append(s[i - 1])
        else:
            mas1.append(s[i - 1])
            mas.append(mas1)
            mas1 = []
    else:
        mas1.append(s[i - 1])

print(mas)

for i in range(len(mas)):
    if isinstance(mas[i], int):
        st.append(str(mas[i]))
    else:
        if len(mas[i]) > 2:
            st.append(str(mas[i][0]) + '-' + str(mas[i][-1]))
        else:
            st.append(str(mas[i][0]))
            st.append(str(mas[i][1]))
st = ','.join(st)
print(st)

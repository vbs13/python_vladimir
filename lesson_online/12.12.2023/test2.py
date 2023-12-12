text = 'Helloworld'
a = {}
for i in text:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
print(a)
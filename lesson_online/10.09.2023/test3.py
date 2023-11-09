def poisk(str, let):
    x = 0
    for i in str:
        if i == let:
            x += 1
    return x

text = 'Hello world'
print(poisk(text, 'l'))
print(text.count('l'))
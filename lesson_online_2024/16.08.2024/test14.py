alf = '0123456789abcdefghij'
for x in alf:
    for y in alf:
        if (int(f'5{y}4{x}{y}4hj4', 20) + int(f'4{y}6b{y}{x}1', 20)) % 15 != 0:
            break
    else:
        print(x)

x = 'h'
y = '8'
f = (int(f'5{y}4{x}{y}4hj4', 20) + int(f'4{y}6b{y}{x}1', 20))
print(f)
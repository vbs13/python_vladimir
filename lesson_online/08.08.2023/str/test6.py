text = input()

for i in range(len(text)):
    if text[i] == '*':
        print(i + 1)
        break
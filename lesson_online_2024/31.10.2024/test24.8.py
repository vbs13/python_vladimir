f = open('C:/Users/Владимир/Downloads/24_17878.txt')
s = f.read()

for i in range(5):
    s = s.replace('-', '*')
    s = s.replace('6', '1').replace('7', '1').replace('8', '1').replace('9', '1')
    s = s.replace('**', ' ')
    s = s.replace('*01', ' 1')
    s = s.replace(' 0', ' ')
    s = s.replace(' *', ' ')
    s = s.replace('* ', ' ')

    # s = s.replace('*0', ' ')
mas = s.split()
print(mas)

print(max([len(x) for x in mas]))
print([x for x in mas if len(x) == 154])
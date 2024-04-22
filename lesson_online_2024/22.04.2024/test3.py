import csv

f = open('C:/Users/Владимир/Desktop/test9.csv')
s = csv.reader(f, delimiter=';')
for i in s:
    q = (list(map(int, i)))
    
print(s)
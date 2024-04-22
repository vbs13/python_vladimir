import csv

f = open('C:/Users/Владимир/Desktop/Таблица_ЕГЭ.csv', 'r', encoding='utf-8')
x = csv.DictReader(f, delimiter=';')

for i in x:
    print(i)

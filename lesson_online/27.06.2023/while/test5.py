price_car = 500000
summ = int(input('Сколько отложить? '))

while price_car <= 0:
    price_car -= summ
    summ = int(input('Сколько отложить? '))

print('купил')
price_1 = int(input())
price_2 = int(input())
price_3 = int(input())
summ = price_1 + price_2 + price_3

if summ > 10000:
    print(summ * 0.9)
else:
    print(summ)
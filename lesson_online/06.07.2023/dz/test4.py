prob1 = 0
ans1 = 0
hour = 1

print('Начался 8-ми часовой рабочий день.')

while hour <= 8:
    print(hour, 'час')
    prob = int(input('Сколько задач решит Максим? '))
    prob1 += prob
    ans = int(input('Звонит жена. Взять трубку? '))
    ans1 += ans
    hour += 1

print('Рабочий день закончился. Всего выполнено задач:', prob1)
if ans1 > 0:
    print('Нужно зайти в магазин')

n = int(input('Кол-во коньков: '))
mas_n = [int(input(f'Размер {x}-й пары: ')) for x in range(1, n + 1)]

k = int(input('Кол-во людей: '))
mas_k = [int(input(f'Размер ноги {x}-го человека: ')) for x in range(1, k + 1)]


mas_nk = []
for i in mas_k:
    if i in mas_n:
        mas_nk.append(i)
        mas_n.remove(i)
print('Наибольшее кол-во людей, которые могут взять ролики:', len(mas_nk))
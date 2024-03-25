violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


st = ['первый', 'второй', 'третий', 'четвертый', 'пятый']

a = int(input('Cколько песен выбрать? '))
summ = 0

for i in range(a):
    print(f'Название {st[i]} песни: ', end='')
    x = input()
    if x in violator_songs:
        summ += violator_songs[x]
print('Общее время звучания песен: ', summ, 'минуты')
mas = [['Medion', '190*53*64'], ['Medion', '220*57*65'], ['Hiesense', '210*59*59']]
for j in range(len(mas) - 1):
    for i in range(len(mas) - 1):
        if mas[i][0] > mas[i + 1][0]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
        elif mas[i][0] == mas[i + 1][0]:
            if mas[i][1] < mas[i + 1][1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)
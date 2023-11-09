bd = []
count = 0
def add_bd():
    global count
    count += 1
    a = []
    detail = input('Введите деталь: ')
    price = int(input('Введите стоимость: '))
    a.append(count)
    a.append(detail)
    a.append(price)
    bd.append(a)


def print_bd():
    print('№ \t Name \t price ')
    for i in range(len(bd)):
        print(bd[i][0], '\t', bd[i][1], '\t', bd[i][2])


def main():
    print('1 - добавить \n2 - вывести \n0 - выход', )
    while True:
        a = int(input('Введите действие: '))
        if a == 0:
            return a
        elif a == 1:
            add_bd()
        elif a == 2:
            print_bd()
# сделать функцию для удаления по имени или по номеру

main()
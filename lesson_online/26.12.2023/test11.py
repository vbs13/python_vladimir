kontact = {}


def add():
    print('\n\nЗапишите имя человека и его номер телефона через пробел: ')
    info = list(input('Введите здесь: ').split())
    if info[0] in kontact:
        print('Такое имя уже есть:')
        n = int(input('Введите 1 если хотите заменить, 0 если оставить: '))
        if n == 1:
            kontact[info[0]] = info[1]
    else:
        kontact[info[0]] = info[1]
    menu()


def menu():
    print('\n\n\t\tТелефонная книга: ')
    print('\t\t1 - вывести список')
    print('\t\t2 - добавить контакт')
    print('\t\t0 - выйти из телефонной книги')
    num = int(input('\t\tВыберите действие: '))
    if num == 0:
         print('Пока')
         return 0
    elif num == 1:
        cout()
    elif num == 2:
        add()


def cout():
    print('\n\nСписок контактов: ')
    print('Имя - номер телефона')
    for i in kontact:
        print(i, '-', kontact[i])
    menu()


menu()
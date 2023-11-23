num1 = int(input('Введите левую границу: '))
num2 = int(input('Введите правую границу: '))

print('Список чисел кубов:', [x**3 for x in range(num1, num2 + 1)])
mas2 = [x * x for x in range(num1, num2 + 1)]
print('Список чисел квадратов:', mas2)
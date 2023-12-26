student = {}
info = list(input().split())

student['Имя'] = info[0]
student['Фамилия'] = info[1]
student['Город'] = info[2]
student['Университет'] = info[3]
student['Оценки'] = info[4:]
print(info)
for i in student:
    print(i, '-', student[i])
s = '1' + '9' * 98
while ('19' in s) or ('299' in s) or ('3999' in s):
    s = s.replace('19', '2', 1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)
print(s)


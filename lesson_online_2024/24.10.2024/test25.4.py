from fnmatch import fnmatch


for n in range(0, 10**10, 4173):
    if fnmatch(str(n), '1?7246*1'):
        print(n)
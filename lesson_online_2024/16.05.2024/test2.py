def tpl_del(a):
    mas = list(a)
    maxx, minn = max(mas), min(mas)
    while maxx in mas:
        mas.remove(maxx)
    while minn in mas:
        mas.remove(minn)
    return tuple(mas)

m = (3, 2, 4, 6, 2)
print(tpl_del(m))
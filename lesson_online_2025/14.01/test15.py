# p = [i/10 for i in range(10, 151)]
# q = [i/10 for i in range(160, 251)]
# r = [i/10 for i in range(240, 301)]
# a = [i/10 for i in range(0, 321)]
#
#
# def f(x):
#     return (((x in q) <= (x in p)) or ((x not in a) <= (x in r)))
#
#
# for x in [i/10 for i in range(0,321)]:
#     if f(x) == False:
#         a.remove(x)
# print(a)


p = 0
q = 0
r = 1
for a in range(0, 2):
    f = ((q <= p) or ((not(a)) <= r))
    print(a, f)

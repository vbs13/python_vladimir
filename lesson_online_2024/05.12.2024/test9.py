# p = 0
# q = 1
# for a in range(2):
#     if (a and q) <= (p or q):
#         print(a)
#
# print(118 - 75)
# print(73 - 25)


b = 0
c = 1
for a in range(2):
    if c <= (((not(a)) and b) <= (not(c))):
        print(a)

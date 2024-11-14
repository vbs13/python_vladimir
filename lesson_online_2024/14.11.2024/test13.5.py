import ipaddress


# for mask in range(32, 0, -1):
#     net = ipaddress.ip_network(f'147.222.199.75/{mask}', 0)
#     for ip in net.hosts():
#         a = str(ip).split('.')
#         if a[0] == a[3] and a[1] == a[2]:
#             print(mask)


k = 0
net = ipaddress.ip_network(f'147.222.199.75/19', 0)
for ip in net.hosts():
    a = str(ip).split('.')
    b = bin(int(a[0])).count('1') + bin(int(a[1])).count('1') + bin(int(a[2])).count('1') + bin(int(a[3])).count('1')
    if b == 14:
        k += 1
print(k)

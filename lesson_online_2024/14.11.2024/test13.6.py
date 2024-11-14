import ipaddress


for mask in range(33):
    net = ipaddress.ip_network(f'224.128.112.142/{mask}', 0)
    if str(net) == f'224.128.64.0/{mask}':
        print(ipaddress)


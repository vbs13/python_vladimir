import ipaddress


for mask in range(0, 33):
    net = ipaddress.ip_network(f'98.162.71.94/{mask}', 0)
    if str(net) == f'98.162.71.64/{mask}':
        print(net, net.num_addresses)

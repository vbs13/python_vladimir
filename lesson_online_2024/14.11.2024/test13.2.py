import ipaddress


net = ipaddress.ip_network('192.168.100.10/29', 0)
print(net)


broadcast_address = net.broadcast_address
print(broadcast_address)


count_host = net.num_addresses - 2
print(count_host)
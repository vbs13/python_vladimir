import ipaddress


net = ipaddress.ip_network('0.0.0.0/255.255.254.0', 0)
print(net.num_addresses - 2)

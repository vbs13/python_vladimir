import ipaddress


ip = ipaddress.ip_network('167.200.37.243/26', strict=False)


# сеть
nerwork_address = ip.network_address
print(nerwork_address)


# широка
broadcast_address = ip.broadcast_address
print(broadcast_address)


for host in ip.hosts():
    print(host)

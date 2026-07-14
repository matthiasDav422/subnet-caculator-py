import ipaddress

def subnet_calculator():
    print("=== Python Subnet Calculator ===\n")
    network = input("Enter network in CIDR format e.g. 192.168.1.0/24: ")
    
    try:
        net = ipaddress.ip_network(network, strict=False)
        
        print(f"\n--- Results for {net} ---")
        print(f"Network Address: {net.network_address}")
        print(f"Broadcast Address: {net.broadcast_address}")
        print(f"Subnet Mask: {net.netmask}")
        print(f"Total Hosts: {net.num_addresses}")
        print(f"Usable Hosts: {net.num_addresses - 2}")
        print(f"Usable Range: {list(net.hosts())[0]} - {list(net.hosts())[-1]}")
        
    except ValueError:
        print("Invalid CIDR format. Example: 192.168.1.0/24")

if __name__ == "__main__":
    subnet_calculator()
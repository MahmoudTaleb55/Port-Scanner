import socket

def scan_ports(ip, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open.")
        sock.close()

target_ip = input("Enter the target IP: ")
port_list = [21, 22, 23, 80, 443, 8080]  # Common ports
scan_ports(target_ip, port_list)
# CyberScan Toolkit
# Module 1 - Port Scanner
# Author: rudranoir0-dot

import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return True
        return False
    except:
        return False

target = input("Enter IP or domain to scan: ")
print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    if scan_port(target, port):
        print(f"[OPEN] Port {port}")

print("\nScan complete.")
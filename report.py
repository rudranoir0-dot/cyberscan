# CyberScan Toolkit
# Module 4 - Report Generator
# Author: rudranoir0-dot

import socket
from datetime import datetime

def scan_ports(target):
    open_ports = []
    for port in range(1, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((target, port))
            sock.close()
            if result == 0:
                open_ports.append(port)
        except:
            pass
    return open_ports

def whois_lookup(domain):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect(("whois.iana.org", 43))
        sock.send((domain + "\r\n").encode())
        response = b""
        while True:
            data = sock.recv(4096)
            if not data:
                break
            response += data
        sock.close()
        return response.decode(errors="ignore")
    except Exception as e:
        return f"Error: {str(e)}"

target = input("Enter target IP or domain: ")
print(f"\nRunning full scan on {target}...")
print("This may take a few minutes...\n")

try:
    ip = socket.gethostbyname(target)
except:
    print("Invalid host")
    exit()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"report_{target}_{timestamp}.txt"

with open(filename, "w") as f:
    f.write("=" * 50 + "\n")
    f.write("       CYBERSCAN TOOLKIT - THREAT REPORT\n")
    f.write("=" * 50 + "\n")
    f.write(f"Target   : {target}\n")
    f.write(f"IP       : {ip}\n")
    f.write(f"Date     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("=" * 50 + "\n\n")

    f.write("[PORT SCAN RESULTS]\n")
    print("Scanning ports...")
    open_ports = scan_ports(ip)
    if open_ports:
        for port in open_ports:
            f.write(f"  [OPEN] Port {port}\n")
            print(f"  [OPEN] Port {port}")
    else:
        f.write("  No open ports found\n")
    
    f.write("\n[WHOIS INFORMATION]\n")
    print("\nFetching WHOIS data...")
    whois = whois_lookup(target)
    f.write(whois)

    f.write("\n" + "=" * 50 + "\n")
    f.write("END OF REPORT\n")
    f.write("=" * 50 + "\n")

print(f"\nReport saved as: {filename}")
print("Scan complete.")
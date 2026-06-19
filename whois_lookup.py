# CyberScan Toolkit
# Module 3 - WHOIS Lookup
# Author: rudranoir0-dot

import socket

def whois_lookup(domain):
    try:
        whois_server = "whois.iana.org"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((whois_server, 43))
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

domain = input("Enter domain to lookup: ")
print(f"\nFetching WHOIS for {domain}...\n")

result = whois_lookup(domain)
print(result)
print("\nLookup complete.")

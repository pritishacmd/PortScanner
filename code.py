import socket

def scan(ip, p1, p2):
    print(f"\nScanning {ip} from port {p1} to {p2}...\n")
    open_p = []

    for p in range(p1, p2 + 1):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            if s.connect_ex((ip, p)) == 0:
                print(f"Port {p} is open")
                open_p.append(p)
            s.close()
        except:
            pass

    if not open_p:
        print("No open ports found.")
    else:
        print(f"\nScan finished. Open ports: {open_p}")

# -------- Main --------
print("Simple Port Scanner")

ip = input("Enter IP: ")
p1 = int(input("Start port: "))
p2 = int(input("End port: "))

scan(ip, p1, p2)
import socket

def tcp_scan(ip, p1, p2):
    print(f"\n[+] Scanning TCP {ip} from port {p1} to {p2}...\n")
    open_p = []

    for p in range(p1, p2 + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((ip, p)) == 0:
                print(f"TCP Port {p} is OPEN")
                open_p.append(p)
            s.close()
        except:
            pass

    if not open_p:
        print("[-] No open TCP ports found.")
    else:
        print(f"\n[✓] TCP Scan finished. Open ports: {open_p}")


def udp_scan(ip, p1, p2):
    print(f"\n[+] Scanning UDP {ip} from port {p1} to {p2}...\n")
    open_p = []

    for p in range(p1, p2 + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(1)
            s.sendto(b"hello", (ip, p))  # send dummy packet

            try:
                data, _ = s.recvfrom(1024)  # reply = open
                print(f"UDP Port {p} is OPEN (response received)")
                open_p.append(p)
            except socket.timeout:
                # Could be open but no reply, or filtered
                print(f"UDP Port {p} is OPEN|FILTERED (no response)")
                open_p.append(p)
            s.close()
        except:
            pass

    if not open_p:
        print("[-] No open UDP ports found.")
    else:
        print(f"\n[✓] UDP Scan finished. Open ports: {open_p}")


# -------- Main --------
print("Simple Port Scanner")
ip = input("Enter IP: ")
p1 = int(input("Start port: "))
p2 = int(input("End port: "))

mode = input("Scan mode (tcp/udp): ").strip().lower()

if mode == "tcp":
    tcp_scan(ip, p1, p2)
elif mode == "udp":
    udp_scan(ip, p1, p2)
else:
    print("Invalid mode. Choose 'tcp' or 'udp'.")

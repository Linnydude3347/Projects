"""
Port Scanner - Enter an IP address and a port range where the program will then attempt
to find open ports on the given computer by connecting to each of them. On any successful
connections mark the port as open.

https://github.com/karan/Projects
"""

import socket
from time import sleep # So we don't bombard websites with constant connection requests

WEBSITE = "https://www.hackthissite.org/"

USUALLY_OPEN_PORTS = [
    20,     # FTP
    22,     # SSH
    25,     # SMTP
    53,     # DNS
    80,     # HTTP
    110,    # P0P3
    143,    # IMAP
    443     # HTTPS
]

ALL_PORTS = range(1, 65536)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in USUALLY_OPEN_PORTS:
    try:
        sock.connect((WEBSITE, port))
        print(f"[OPEN]:\t{port}")
    except:
        continue
    sleep(0.5)

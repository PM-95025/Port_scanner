import socket
from typing import Final
from colorama import init, Fore
from net import check_connect, scan

init()
GREEN: Final[str] = Fore.GREEN
RESET: Final[str] = Fore.RESET

check_connect()

host: Final[str] = input('host: ')
socket.setdefaulttimeout(float(input('timeout: ')))

with open('ports.txt') as f:
	lines = f.readlines()

ports: Final[tuple[int]] = tuple([int(i.split()[0]) for i in lines])
types: Final[tuple[str]] = tuple([i.split()[1] if len(i.split()) > 1 else '' for i in lines])
info: Final[tuple[str]] = tuple([' '.join(i.split()[2:]) for i in lines])

print(f'will be checked {len(ports)} ports')

opened: list[int] = scan(host, ports)

for port in sorted(opened):
	i = ports.index(port)
	print(f"{GREEN}{host:15}:{port:5} is open{RESET} - {types[i]:10} - {info[i] if info[i] else 'unknown'}")

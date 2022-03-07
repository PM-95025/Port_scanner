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
	ports: Final[tuple[int]] = tuple([int(i) for i in f.readlines()])
	print(f'will be checked {len(ports)} ports')

opened: set[int] = scan(host, ports)

print(', '.join([str(i) for i in list(opened)]))

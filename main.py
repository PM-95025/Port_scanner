import socket
from typing import Final, Iterable
from colorama import init, Fore
import sys
from tqdm import tqdm

init()
GREEN: Final[str] = Fore.GREEN
RESET: Final[str] = Fore.RESET

opened: set[int] = set()

try:
	socket.socket().connect(('8.8.8.8', 53))
except socket.error:
	print("This script requires established interned connection!")
	sys.exit()


host: Final[str] = input('host: ')
socket.setdefaulttimeout(float(input('timeout: ')))


def port_scan(port: int) -> bool:
	s: socket = socket.socket()
	try:
		s.connect((host, port))
	except (ConnectionError, TimeoutError):
		return False
	else:
		return True
	finally:
		s.close()


def scan(ports_: Iterable[int]) -> None:
	for port in list(ports_):
		connected: bool = port_scan(port)
		if connected:
			opened.add(port)
			print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")


with open('ports.txt') as f:
	ports: Final[tuple[int]] = tuple([int(i) for i in f.readlines()])
	print(f'will be checked {len(ports)} ports')

scan(ports)
print(', '.join([str(i) for i in list(opened)]))

import socket
from typing import Iterable
from colorama import init, Fore
from tqdm import tqdm

init()
GREEN = Fore.GREEN
RESET = Fore.RESET

opened: set[int] = set()

host = input('host: ')
socket.setdefaulttimeout(__timeout=float(input('timeout: ')))


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
		if port_scan(port):
			opened.add(port)
			print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")
		pass


with open('ports.txt') as f:
	ports: tuple[int] = tuple([int(i) for i in f.readlines()])
	print(f'will bo checked {len(ports)} ports')

scan(ports)
print(', '.join([str(i) for i in list(opened)]))

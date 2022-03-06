import socket
from typing import Iterable, Union
from colorama import init, Fore
from tqdm import tqdm

init()
GREEN = Fore.GREEN
RESET = Fore.RESET

opened: set[int] = set()

host = input('host: ')
socket.setdefaulttimeout(float(input('timeout: ')))


def port_scan(port: int) -> Union[bool, str]:
	s: socket = socket.socket()
	try:
		s.connect((host, port))
	except (ConnectionError, TimeoutError):
		return False
	except OSError:
		print('No internet connection!')
		return 'no'
	else:
		return True
	finally:
		s.close()


def scan(ports_: Iterable[int]) -> None:
	for port in list(ports_):
		state = port_scan(port)
		if state == 'no':
			return
		elif not state:
			pass
		else:
			opened.add(port)
			print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")


with open('ports.txt') as f:
	ports: tuple[int] = tuple([int(i) for i in f.readlines()])
	print(f'will be checked {len(ports)} ports')

scan(ports)
print(', '.join([str(i) for i in list(opened)]))

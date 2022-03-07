from typing import Final, Iterable
from colorama import init, Fore
from tqdm import tqdm

from net import port_scan

init()
GREEN: Final[str] = Fore.GREEN
RESET: Final[str] = Fore.RESET


def scan(host, ports_: Iterable[int]) -> set[int]:
	opened: set[int] = set()

	for port in tqdm(ports_):
		connected: bool = port_scan(host, port)
		if connected:
			opened.add(port)
			print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")
	return opened

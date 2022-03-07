from typing import Final, Iterable
from colorama import init, Fore
from tqdm import tqdm

from net import port_scan

init()
GREEN: Final[str] = Fore.GREEN
RESET: Final[str] = Fore.RESET


def scan(host, ports_: Iterable[int]) -> list[int]:
	opened: list[int] = []

	for port in tqdm(ports_):
		connected: bool = port_scan(host, port)
		if connected:
			opened.append(port)
	return opened

from random import choice
from typing import Final, Union
from net import port_scan
from colorama import init, Fore

init()
GREEN: Final[str] = Fore.GREEN
RESET: Final[str] = Fore.RESET


def scan_random(host, ports_: Union[list[int], tuple[int]]) -> None:
	from main import opened

	for i in tqdm(range(len(ports_))):
		port = choice(ports_)
		connected: bool = port_scan(host, port)
		if connected:
			opened.add(port)
			print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")
		ports_.remove(port)

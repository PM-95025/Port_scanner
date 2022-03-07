import socket
import sys


def check_connect() -> None:
	try:
		socket.socket().connect(('8.8.8.8', 53))
	except socket.error:
		print("This script requires established interned connection!")
		sys.exit()

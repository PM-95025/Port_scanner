import socket


def port_scan(host, port: int) -> bool:
	s: socket = socket.socket()
	try:
		s.connect((host, port))
	except (ConnectionError, TimeoutError):
		return False
	else:
		return True
	finally:
		s.close()

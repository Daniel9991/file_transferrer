import socket
from file_transferrer.constants import ENCODING


class Server:

	def __init__(self, ip_address, port):
		"""Creates a server so that another device may connect to it."""

		self.ip_address = ip_address
		self.port = port

		self.create_server()
		self.accept_connection()


	def create_server(self):
		"""Creates the server socket."""

		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_socket.bind((self.ip_address, self.port))
		self.server_socket.listen()


	def accept_connection(self):
		"""Accepts connection"""

		self.connection, address = self.server_socket.accept()
		print(f"Received connection from {address}")


	def send_message(self, message):
		"""Handles message sending over the connection"""

		if type(message) == bytes:
			pass
		elif type(message) == str:
			message = message.encode(ENCODING)
		else:
			raise TypeError("Message must be str or bytes")

		try:
			self.connection.send(message)
		except Exception as e:
			print("There was an exception")
			print(e)
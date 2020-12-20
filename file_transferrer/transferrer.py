class Transferrer:

	def __init__(self, connection):
		"""This is the class in charge of transferring and receiving files and directories,
		and it uses a socket connection for that."""

		self.conneciton = connection
import tkinter as tk



class App(tk.Tk):

	
	def __init__(self):
		"""Root for all screens and frames of the app."""

		super().__init__()
		self.title('CopyMe')
		
		label = tk.Label(self, text="We will help you transfer some files.")
		label.pack(pady=(10,10), padx=(5,5))

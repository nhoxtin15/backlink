
from PyQt5.QtWidgets import QTextEdit, QListView, QVBoxLayout


class frontPage (QWidget):
	

	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle('FrontPage')
		self.setGeometry(100, 100,1000 , 800)


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTextEdit, QListView, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    

    def initUI(self):
        self.setWindowTitle('BackLink')
        self.setGeometry(100, 100, 1000, 800)  # (x, y, width, height)

        hBox = QHBoxLayout(self)

        # Create a QTextEdit for the text area
        self.textArea = QTextEdit(self)
        self.textArea.setPlaceholderText("Enter your text here")

        hBox.addWidget(self.textArea)

        # Create a QListView for the list of text files
        self.listView = QListView(self)
        hBox.addWidget(self.listView)
        self.listView.setFixedWidth(200)
        self.listView.setFixedHeight(500)
        self.listView.setSpacing(5)
        self.listView.setUniformItemSizes(True)
        self.listView.setResizeMode(QListView.Adjust)
        self.listView.setMovement(QListView.Static)
        self.listView.setFlow(QListView.TopToBottom)
        self.listView.setWrapping(True)
        # Create a QStandardItemModel
        model = QStandardItemModel(self.listView)

        # Create a QStandardItem
        item = QStandardItem("File 1")
        model.appendRow(item)
        self.listView.setModel(model)
        item1 = QStandardItem("File 2")
        model.appendRow(item1)
        self.setLayout(hBox)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


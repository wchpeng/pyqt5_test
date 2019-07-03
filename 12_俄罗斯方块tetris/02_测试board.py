import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame


class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.tboard = Board(self)
        self.tboard.setStyleSheet("QFrame { background-color: #4d4d4d }")
        # self.setCentralWidget(self.tboard)
        self.tboard.setGeometry(100, 100, 100, 100)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('board')
        self.show()


class Board(QFrame):

    msg3Statusbar = pyqtSignal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



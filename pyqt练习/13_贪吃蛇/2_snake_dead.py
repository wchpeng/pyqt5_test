import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout)

WIDTH = 10
HEIGHT = 10


class SnakeDead(QWidget):

    def __init__(self):
        super(SnakeDead, self).__init__()
        self.init_ui()

    def init_ui(self):

        tips = QLabel('GAME OVER 重新开始？')
        tips.setFont(QFont('SansSerif', 13))

        self.ok = QPushButton('确认')
        self.cancel = QPushButton('退出')

        grid = QGridLayout()
        grid.addWidget(self.ok, 0, 0)
        grid.addWidget(self.cancel, 0, 1)

        vbox = QVBoxLayout()
        vbox.addWidget(tips)
        vbox.addLayout(grid)

        self.setLayout(vbox)
        self.resize(10*15, 10*15)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sd = SnakeDead()
    sys.exit(app.exec_())

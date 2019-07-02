# sender
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        btn1 = QPushButton('Button 001', self)
        btn1.move(30, 30)

        btn2 = QPushButton('Button 002', self)
        btn2.move(30, 160)

        btn3 = QPushButton('Button 003', self)
        btn3.move(160, 30)

        btn4 = QPushButton('Button 004', self)
        btn4.move(160, 160)

        # 将四个按钮的clicked 连接到了同一个插槽 self.buttonClicked
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)
        btn4.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('事件发送者')
        self.show()

    def buttonClicked(self):
        # 信号插槽，通过 self.sender() 来判断信号源，并将其名称显示在 状态栏里
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

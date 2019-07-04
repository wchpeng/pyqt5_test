import sys

from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        red_btn = QPushButton('Red', self)
        red_btn.setCheckable(True)
        red_btn.move(10, 10)
        # 将 clicked 信号连接到用户自定义的方法，通过 clicked 信号操作一个布尔值
        red_btn.clicked[bool].connect(self.set_square_color)

        blue_btn = QPushButton('Blue', self)
        blue_btn.setCheckable(True)
        blue_btn.move(10, 60)
        blue_btn.clicked[bool].connect(self.set_square_color)

        green_btn = QPushButton('Green', self)
        green_btn.setCheckable(True)
        green_btn.move(10, 110)
        green_btn.clicked[bool].connect(self.set_square_color)

        self.col = QColor(0, 0, 0)
        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        self.setGeometry(100, 100, 500, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('开关按钮 checkable=True')
        self.show()

    def set_square_color(self, pressed):
        print("pressed: ", pressed)
        if pressed:
            val = 255
        else:
            val = 0

        sender = self.sender()
        if sender.text() == "Red":
            self.col.setRed(val)  # 更新红色的部分
        elif sender.text() == "Blue":
            self.col.setBlue(val)
        else:
            self.col.setGreen(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

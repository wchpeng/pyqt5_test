import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        lab1 = QLabel('zero', self)
        lab1.move(10, 10)

        lab2 = QLabel('one', self)
        lab2.move(130, 130)

        lab3 = QLabel('two', self)
        lab3.move(250, 250)

        self.setGeometry(70, 70, 400, 400)
        self.setWindowTitle('three labels')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

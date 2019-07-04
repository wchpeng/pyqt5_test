import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(70, 70, 400, 400)
        # self.resize(500, 800)

        # 设置标题
        self.setWindowTitle('snake')

        # 设置小 icon
        self.setWindowIcon(QIcon('01.jpg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# 状态栏用于显示状态信息
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStatusBar
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        # self.statusBar() 第一次调用会创建一个状态栏，后面调用会返回状态栏对象
        # showMessage 会给状态栏显示内容
        self.statusBar().showMessage('Ready')

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('状态栏')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

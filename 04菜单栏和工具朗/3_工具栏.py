import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.toolbar = None
        self.init_ui()

    def init_ui(self):
        exit_action = QAction(QIcon('./02exit.jpg'), '退出', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)

        # 添加工具栏
        self.toolbar = self.addToolBar('Exit01')
        self.toolbar.addAction(exit_action)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('工具栏')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

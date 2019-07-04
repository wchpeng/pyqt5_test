import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 创建一个菜单的一项
        exit_action = QAction(QIcon('02exit.jpg'), '&退出', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)  # qApp.quit 是终结程序

        # self.statusBar().showMessage('Go')

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 创建一个菜单
        file_menu = menubar.addMenu('&menu007')
        file_menu.addAction(exit_action)  # 给菜单添加动作
        # menubar.addMenu('&menu008')

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('菜单栏')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

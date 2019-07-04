import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, qApp


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        # 把整个窗口设置为一个输入框 textEdit
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)

        # 显示界面时在状态栏显示的内容
        self.statusBar().showMessage('Go')

        exit_action = QAction(QIcon('./02exit.jpg'), '退出', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('exit application')  # 鼠标移动到这条‘动作’时会在状态栏显示的内容
        exit_action.triggered.connect(qApp.quit)

        # 添加工具栏
        self.toolbar = self.addToolBar('exit bar')
        self.toolbar.addAction(exit_action)

        # 添加菜单栏
        menubar = self.menuBar()
        menu1 = menubar.addMenu('menu1')
        menu1.addAction(exit_action)

        self.setGeometry(100, 100, 300, 300)  # 设置窗口大小
        self.setWindowTitle('工具、菜单、状态栏')  # 设置标题
        self.setWindowIcon(QIcon('./01.jpg'))  # 设置 icon
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

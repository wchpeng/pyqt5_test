import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MyCommunicate(QObject):
    # 创建一个信号类，closeApp 是他的一个信号
    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.c = MyCommunicate()
        self.c.closeApp.connect(self.close)  # 把 self.c.closeApp 信号绑定到 self.close 上

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('发出信号')
        self.show()

    def mousePressEvent(self, event):
        # 当鼠标点击窗口的时候会触发
        self.c.closeApp.emit()  # 这句是执行 self.c 的 closeApp 信号

    def closeEvent(self, event):
        # 退出事件，退出的时候会拦截调用
        reply = QMessageBox.question(self, 'Message Quit',
                "你确定退出？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

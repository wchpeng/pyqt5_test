import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('重新实现按键处理器')
        self.show()

    def keyPressEvent(self, event):
        # 当有按键被触发时的事件处理
        if event.key() == Qt.Key_Escape:  # 如果按下了键盘的 esc 键，关闭 application
            self.close()

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

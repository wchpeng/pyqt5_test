import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog, QLineEdit


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        dialog_btn = QPushButton('对话框 dialog', self)
        dialog_btn.move(30, 30)
        dialog_btn.clicked.connect(self.show_dialog)

        self.le = QLineEdit(self)
        self.le.move(130, 30)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('对话框 dialog')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()

    def show_dialog(self, evnet):
        # 显示一个对话框，并把输入的数据放到 le 中
        text, ok = QInputDialog.getText(self, 'dialog', 'enter your name: ')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

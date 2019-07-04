import sys

from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFrame


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        dialog_btn = QPushButton('对话框 color dialog', self)
        dialog_btn.move(30, 30)
        dialog_btn.clicked.connect(self.show_dialog)

        col = QColor(0, 0, 0)  # 初始化颜色为黑色

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(30, 100, 100, 100)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('对话框 dialog')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()

    def show_dialog(self, evnet):
        col = QColorDialog.getColor()  # 弹出颜色对话框

        if col.isValid():
            print("col.name(): ", col.name())
            # 改变 frm 的背景颜色
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

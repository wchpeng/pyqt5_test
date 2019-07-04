import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QApplication, QFontDialog, QPushButton, QLabel, QVBoxLayout, QSizePolicy
)


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        # 第一种方法： 字体放大时会显示不全
        # font_btn = QPushButton('字体选择', self)
        # font_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # font_btn.move(30, 30)
        # font_btn.clicked.connect(self.showDialog)
        #
        # self.lab = QLabel('jslkfslkdfd的佛挡杀佛但是方式', self)
        # self.lab.move(30, 130)

        # 第二种方法
        vbox = QVBoxLayout()
        font_btn = QPushButton('字体选择', self)
        font_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        font_btn.clicked.connect(self.showDialog)

        self.lab = QLabel('jslkfslkdfd的佛挡杀佛但是方式', self)

        vbox.addWidget(font_btn)
        vbox.addWidget(self.lab)

        self.setLayout(vbox)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('字体对话框')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()

    def showDialog(self, event):

        font, ok = QFontDialog.getFont()  # 弹出一个字体框，选择字体之后 ok 返回 True
        if ok:
            self.lab.setFont(font)

        # 打开文件选择框
        # fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        # fname[0] 就是选择文件的名字（如果有值的话）


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

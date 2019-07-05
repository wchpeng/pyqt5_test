import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 新建连个按钮 ok 和 cancel
        ok_btn = QPushButton('ok')
        cancel_btn = QPushButton('cancel')
        mid = QPushButton('middle')

        # 水平盒子 HBoxLayout horizontal
        hbox = QHBoxLayout()  # 新建水平盒子
        # 撑大(加上了之后变成了右对齐，不加的话，格子一样大且居中)
        hbox.addStretch(1)    # 加了一个伸展因子，推动按钮向右伸展一个单位，让按钮向右靠齐
        hbox.addWidget(ok_btn)
        hbox.addWidget(cancel_btn)
        # hbox.addWidget(mid)

        # 垂直盒子 VBoxLayout vertical
        vbox = QVBoxLayout()
        vbox.addStretch(1)  # 垂直方向加了一个伸展因子，让按钮向下靠齐
        # vbox.addWidget(mid)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        # self.setLayout(hbox)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('vbox and hbox buttoms')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        sld = QSlider(Qt.Horizontal, self)  # 初始化水平滑块
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.change_sld_value)  # 值改变的事件

        self.lab = QLabel(self)
        self.lab.setPixmap(QPixmap('volume_0.ico'))  # 设置 ico 文件的大小
        self.lab.setGeometry(160, 40, 30, 30)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('滑动条 slider')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()

    def change_sld_value(self, value):
        if value > 50:
            self.lab.setPixmap(QPixmap('volume_high.ico'))
        elif value > 0:
            self.lab.setPixmap(QPixmap('volume_low.ico'))
        else:
            self.lab.setPixmap(QPixmap('volume_0.ico'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QApplication, QLCDNumber, QSlider, QVBoxLayout
)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        lcd = QLCDNumber(self)  # 一个控件，该空间用于显示一个带有类似液晶显示屏效果的数字
        sld = QSlider(Qt.Horizontal, self)  # 滚动条

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)  # 将滚动条的 valueChanged 信号连接到 lcd 的 display 插槽

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon("./01.jpg"))
        self.setWindowTitle('时间和信号槽')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

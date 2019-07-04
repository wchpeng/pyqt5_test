import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        QToolTip.setFont(QFont('Sanserif', 10))  # 提示的字体：10px 滑体
        # QToolTip.setFont()
        self.setToolTip('dddddddd')

        # 创建一个 pushbutton 并为他设置一个 tooltip
        btn = QPushButton('Button007', self)
        btn.setToolTip('This is a <s>QPushButton Button007</s> widget')

        # btn.sizeHint() 显示默认尺寸
        btn.resize(btn.sizeHint())

        # 移动窗口的位置
        btn.move(20, 30)

        self.setGeometry(70, 70, 400, 400)
        self.setWindowTitle('snake tooltip')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

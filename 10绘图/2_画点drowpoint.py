import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('画点 drawPoint')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()

    def paintEvent(self, e):
        # 每次改变窗口的大小，会生成一个 paint event 事件，调用这个方法
        qp = QPainter()
        qp.begin(self)
        self.draw_points(qp)
        qp.end()

    def draw_points(self, qp):
        qp.setPen(Qt.red)  # 设置画笔为红色
        size = self.size()  # 获取窗口尺寸

        for i in range(100):
            # size.width() 获取屏幕尺寸宽，size.height() 获取高
            # 找 x，y 点，调用 drawPoint 方法画点
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

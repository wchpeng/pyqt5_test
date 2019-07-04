import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):

    def __init__(self):

        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('画笔')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_lines(qp)
        qp.end()

    def draw_lines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)  # 钢笔样式 2px 黑色

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        # 以下是五种风格的钢笔
        pen.setStyle(Qt.DashLine)  # 虚线
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)  # 虚+点线
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)  # 点线
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)  # 虚+点+点线
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)  # 自定义了一个形状

        # 第一个数 1 表示 1px 实点的宽度，第二个数 4 表示 4px 的空白
        # 第三个数 5 表示 5px 实点的宽度，第四个数 4 表示 4px 的空白
        # 我们可以增加或减少列表里的数字
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# 化矩形并填充颜色，左上边是light，右下边是黑边
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):

    def __init__(self):

        super(Example, self).__init__()
        self.x = 150
        self.y = 150
        self.m = 25
        self.n = 25
        self.init_ui()

    def init_ui(self):

        rotate_left_btn = QPushButton('up', self)
        rotate_left_btn.clicked.connect(self.rotate_up)
        rotate_left_btn.move(40, 10)

        rotate_left_btn = QPushButton('down', self)
        rotate_left_btn.clicked.connect(self.rotate_down)
        rotate_left_btn.move(40, 90)

        rotate_right_btn = QPushButton('left', self)
        rotate_right_btn.clicked.connect(self.rotate_left)
        rotate_right_btn.move(0, 50)

        rotate_right_btn = QPushButton('right', self)
        rotate_right_btn.clicked.connect(self.rotate_right)
        rotate_right_btn.move(90, 50)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('画笔')
        self.show()

    def rotate_up(self, e):
        self.y -= 20
        self.update()  # update 是更新窗口

    def rotate_down(self, e):
        self.y += 20
        self.update()

    def rotate_left(self, e):
        self.x -= 20
        self.update()

    def rotate_right(self, e):
        self.x += 20
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()

    def draw_line(self, qp):
        self.draw_item(qp, self.x, self.y, self.m, self.n)
        self.draw_item(qp, self.x+self.m, self.y, self.m, self.n)
        # self.draw_item(qp, self.x, 35, 25, 25)
        self.draw_item(qp, self.x+self.m, self.y+self.n, self.m, self.n)
        self.draw_item(qp, self.x+self.m, self.y+2*self.n, self.m, self.n)

    def draw_item(self, qp, x, y, m, n):
        # x 10, y 10, z 25, w: 25

        color = QColor(0xCCCC66)
        qp.fillRect(x+1, y+1, m-2, n-2, color)

        qp.setPen(color.lighter())
        qp.drawLine(x, y+n-1, x, y)
        qp.drawLine(x, y, x+m-1, y)

        qp.setPen(color.darker())
        qp.drawLine(x+1, y+n-1, x+m-1, y+n-1)
        qp.drawLine(x+n-1, y+n-1, x+m-1, y+1)

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

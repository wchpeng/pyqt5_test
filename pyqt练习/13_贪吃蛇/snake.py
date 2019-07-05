import sys
import random

from PyQt5.QtCore import pyqtSignal, Qt, QBasicTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame


class Snake(QMainWindow):

    def __init__(self):
        super(Snake, self).__init__()
        self.init_ui()
        self.init_board()

    def init_ui(self):

        self.setGeometry(100, 100, 15*Board.WIDTH, 15*Board.HEIGHT+25)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('贪吃蛇')
        self.show()

    def init_board(self):
        self.statusBar().showMessage("欢迎进入贪吃蛇")
        self.board = Board(self)
        self.board.msg2status_bar[str].connect(self.statusBar().showMessage)
        self.setCentralWidget(self.board)
        self.setFocusPolicy(Qt.StrongFocus)
        self.board.setStyleSheet('QFrame { background-color: #4d4d4d }')
        self.board.start()


class Board(QFrame):

    msg2status_bar = pyqtSignal(str)
    SPEED = 400
    WIDTH = 30
    HEIGHT = 30

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.timer = QBasicTimer()

        self.node = Node()

    def start(self):
        self.timer.start(self.SPEED, self)

    def timerEvent(self, e):
        if e.timerId() != self.timer.timerId():
            return super(Board, self).timerEvent(e)
        self.snake_walk()

    def snake_walk(self):
        # 蛇每次走一步
        pass

    def board_cube_width(self):
        print(self.contentsRect())
        return 15
        return self.contentsRect().width() // self.WIDTH

    def board_cube_height(self):
        print(self.contentsRect().width())
        print(self.contentsRect().height())
        return 15
        return self.contentsRect().height() // self.HEIGHT


class Node(object):

    def __init__(self):
        self.star_x = 0
        self.star_y = 0
        self.direct_x = 1  # 初始为向左水平运动
        self.direct_y = 0  # 初始 y 轴不变
        self.nodes = [(Board.WIDTH // 2, Board.HEIGHT//2)]  # 存放蛇的每一节的坐标，定义初始点
        self.nodes_set = {(Board.HEIGHT//2)*Board.WIDTH + Board.WIDTH//2}  # 存放坐标转化为int

        self.waiting_new_star = True  # 等待新的'星'

    def remove_tail(self):
        x, y = self.nodes.pop()
        coordinate2int = self.coordinate2int(x, y)
        if coordinate2int in self.nodes_set:
            self.nodes_set.remove(coordinate2int)

    def coordinate_in_nodes_set(self, x, y):
        return self.coordinate2int(x, y) in self.nodes_set

    def add2head(self, x, y):
        self.nodes.insert(0, (x, y))
        self.nodes_set.add(self.coordinate2int(x, y))

    @staticmethod
    def coordinate2int(x, y):
        return y*Board + x

    def set_new_star(self):
        x = random.randint(0, Board.WIDTH - 1)
        y = random.randint(0, Board.HEIGHT - 1)
        if self.coordinate_in_nodes_set(x, y):
            return self.set_new_star()
        else:
            self.star_x, self.star_y = x, y

    def walk(self, cur_x, cur_y):
        x = cur_x + self.direct_x
        y = cur_y + self.direct_y

        if self.coordinate_in_nodes_set(x, y):
            # 撞到了自己
            return False

        if x < 0 or x > Board.WIDTH or y < 0 or y > Board.HEIGHT:
            # 撞到了边界
            return False

        self.add2head(x, y)
        if x == self.star_x and y == self.star_y:
            self.waiting_new_star = True
            return True

        self.remove_tail()
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    snake = Snake()
    sys.exit(app.exec_())

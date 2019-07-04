import sys
import time
import copy
import random

from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtCore import pyqtSignal, QBasicTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFrame

SPEED = 500  # ms
WIDTH_GRID = 20
HEIGHT_GTID = 40


class Tetris(QMainWindow):
    # 主窗口：设置窗口大小和菜单栏/状态栏

    def __init__(self):
        super(Tetris, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.init_tboard()

        restart_action = QAction(QIcon('restart.jpg'), '&重新开始', self)
        restart_action.setShortcut('Ctrl+R')
        restart_action.triggered.connect(self.restart_tetris)

        menu = self.menuBar().addMenu('设置')
        menu.addAction(restart_action)

        self.setGeometry(100, 100, 15*WIDTH_GRID, 15*HEIGHT_GTID)
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setWindowTitle('俄罗斯方块 tetris')
        self.show()

    def restart_tetris(self):
        print("restart tetris")
        pass

    def init_tboard(self):
        # 俄罗斯方块的一切逻辑操作在这里（旋转控制/满层消除/gameover判断/定时器判断/图形渲染）
        self.statusBar().showMessage("欢迎加入游戏")
        self.tboard = Board(self)
        self.tboard.msg2status_bar.connect(self.statusBar().showMessage)
        self.setCentralWidget(self.tboard)
        self.tboard.setStyleSheet("QFrame { background-color:#dedede }")
        self.tboard.start()


class Board(QFrame):
    # 俄罗斯方块的一切逻辑操作在这里（旋转控制/满层消除/gameover判断/定时器判断/图形渲染）
    msg2status_bar = pyqtSignal()

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.is_paused = False  # 是否被暂停
        self.num_lines_removed = 0  # 被删除的行数

        self.cur_x = 0
        self.cur_y = 0
        self.cur_shape = None

        self.timer = QBasicTimer()
        self.boards = []
        self.clear_board()

    def clear_board(self):
        self.boards = [(0, 0) for i in range(WIDTH_GRID*HEIGHT_GTID)]

    def start(self):
        self.new_shape()
        self.timer.start(SPEED, self)

    def timerEvent(self, e):
        print(e)
        print("timer work", time.time())
        self.shape_down1line(0, 1)
        self.draw_shape()

    def new_shape(self):
        # 新建 shape
        self.cur_x = WIDTH_GRID // 2 - 0.5
        self.cur_y = 0
        self.cur_shape = Shape()
        self.cur_shape.set_random_shape()
        self.draw_shape()

    def shape_down1line(self, x_offset, y_offset):
        # shape 往下移动一行
        if self.move_shape(self.cur_shape.move(x_offset, y_offset), x_offset, y_offset):
            self.update()

    def shape_drop_down(self):
        # 直接移动到底部
        while self.shape_down1line(0, 1):
            pass

    def shape_pause(self):
        if self.is_paused:
            self.timer.start(SPEED)
            self.msg2status_bar.emit("分数：" + str(self.num_lines_removed))
        else:
            self.timer.stop()
            self.msg2status_bar.emit("暂停")

        self.is_paused = not self.is_paused
        self.update()

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Up:
            # 上：左转
            pass
        elif key == Qt.Key_Down:
            # 下：右转
            pass
        elif key == Qt.Key_Left:
            # 左移
            self.shape_down1line(-1, 0)
        elif key == Qt.Key_Right:
            # 右移
            self.shape_down1line(1, 0)
        elif key == Qt.Key_P:
            # 暂停
            self.shape_pause()
        elif key == Qt.Key_Space:
            # 空格：直接下到最后一行
            self.shape_drop_down()

    def move_shape(self, shape, x_offset, y_offset):
        for i in range(len(shape.coors)):
            x = shape.get_x(i) + self.cur_x
            y = shape.get_y(i) + self.cur_y

            if x < 0 or x >= WIDTH_GRID or y < 0 or y > HEIGHT_GTID:
                # 设定不能超出边界
                return False
            if self.boards[self.get_index_in_boards(x, y)] != ShapeType.No_shape:
                # 如果 x y 这个坐标在 boards 中不是空形状，返回 False
                return False

        self.cur_x += x_offset
        self.cur_y += y_offset
        self.cur_shape = shape
        self.update()
        return True

    @classmethod
    def get_index_in_boards(cls, x, y):
        return y * WIDTH_GRID + x

    def draw_shape(self):
        qp = QPainter()
        qp.begin(self)
        for i in range(len(self.cur_shape.coors)):
            pass

        qp.end()

    def painter_square(self, x, y):
        qp = QPainter()
        qp.begin(self)

        qp.end()

class ShapeType:
    Coors_table = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1))
    )

    No_shape = 0
    Z_shape = 1
    S_shape = 2
    Line_shape = 3
    T_shape = 4
    Square_shape = 5
    L_shape = 6
    Mirrored_L_shape = 7


class Shape(object):

    def __init__(self):
        self.coors = ((0, 0), (0, 0), (0, 0), (0, 0))
        self.shape_type = 0

    def set_random_shape(self):
        self.shape_type = random.randint(1, len(ShapeType.Coors_table))
        self.coors = copy.deepcopy(ShapeType.Coors_table[self.shape_type])
        return self.shape_type

    def set_shape_coors(self, shape_type):
        self.shape_type = shape_type
        self.coors = copy.deepcopy(ShapeType.Coors_table[shape_type])

    def set_x(self, index, x):
        self.coors[index][0] = x

    def get_x(self, index):
        return self.coors[index][0]

    def set_y(self, index, y):
        self.coors[index][1] = y

    def get_y(self, index):
        return self.coors[index][1]

    def move(self, x_offset, y_offset):
        # 水平、垂直 移动，传入每次移动的偏移量
        shape = Shape()
        shape.set_shape_coors(self.shape_type)
        for i in self.coors:
            shape.set_x(i, shape.get_x(i) + x_offset)
            shape.set_y(i, shape.get_y(i) + y_offset)
        return shape

    def rotate_left(self):
        # 向左旋转 90 度
        shape = Shape()
        shape.set_shape_coors(self.shape_type)
        for i in range(len(shape.coors)):
            shape.set_x(i, -shape.get_y(i))
            shape.set_y(i, shape.get_x(i))
        return shape

    def rotate_right(self):
        # 向右旋转 90 度
        shape = Shape()
        shape.set_shape_coors(self.shape_type)
        for i in range(len(shape.coors)):
            shape.set_x(i, shape.get_y(i))
            shape.set_y(i, -shape.get_x(i))
        return shape
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetris = Tetris()
    sys.exit(app.exec_())

import sys
import copy
import random

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal, QBasicTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFrame

SPEED = 300  # ms
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
        print("timer work")

    def new_shape(self):
        self.cur_x = WIDTH_GRID // 2 - 0.5
        self.cur_y = HEIGHT_GTID
        self.cur_shape = Shape()


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

    def set_shape_coors(self, shape_type):
        self.coors = copy.deepcopy(ShapeType.Coors_table[shape_type])

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetris = Tetris()
    sys.exit(app.exec_())

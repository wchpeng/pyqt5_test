import sys
import time
import random

from PyQt5.QtGui import QIcon, QPainter, QColor
from PyQt5.QtCore import pyqtSignal, QBasicTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFrame

SPEED = 700  # ms
WIDTH_GRID = 13
HEIGHT_GRID = 26


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

        self.setGeometry(100, 100, 15*WIDTH_GRID, 15*HEIGHT_GRID + 45)  # +45 是因为底部状态栏
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setWindowTitle('俄罗斯方块 tetris')
        self.show()

    def restart_tetris(self):
        print("restart tetris")
        self.init_tboard()

    def init_tboard(self):
        # 俄罗斯方块的一切逻辑操作在这里（旋转控制/满层消除/gameover判断/定时器判断/图形渲染）
        self.statusBar().showMessage("欢迎加入游戏")
        self.tboard = Board(self)
        self.tboard.msg2status_bar[str].connect(self.statusBar().showMessage)
        self.setCentralWidget(self.tboard)
        self.tboard.setStyleSheet("QFrame { background-color:#dedede }")
        self.tboard.start()


class Board(QFrame):
    # 俄罗斯方块的一切逻辑操作在这里（旋转控制/满层消除/gameover判断/定时器判断/图形渲染）
    msg2status_bar = pyqtSignal(str)

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.is_paused = False  # 是否被暂停
        self.num_lines_removed = 0  # 被删除的行数
        self.game_start = True
        self.waiting_new_shape = False

        self.cur_x = 0
        self.cur_y = 0
        self.cur_shape = None

        self.setFocusPolicy(Qt.StrongFocus)  # 界面没有按钮时，设置聚焦
        self.timer = QBasicTimer()
        self.boards = []
        self.clear_board()

    def clear_board(self):
        self.boards = [0 for i in range(WIDTH_GRID*HEIGHT_GRID)]

    def start(self):
        self.new_shape()
        self.timer.start(SPEED, self)

    def paintEvent(self, e):
        self.draw_shape()

    def new_shape(self):
        # 新建 shape
        self.cur_x = WIDTH_GRID // 2
        self.cur_y = 0
        self.cur_shape = Shape()
        self.cur_shape.set_random_shape()
        self.cur_shape.set_shape_coors(self.cur_shape.shape_type)

        if not self.move_shape(self.cur_shape, 0, 1):
            self.timer.stop()
            self.msg2status_bar.emit('Game Over!')
            self.game_start = False
            if self.cur_shape_has_repeat():
                self.cur_shape = Shape()
        self.update()

    def cur_shape_has_repeat(self):
        for i in range(len(self.cur_shape.coors)):
            x = self.cur_shape.get_x(i)
            y = self.cur_shape.get_y(i)
            if self.get_shape_in_boards(x, y) != ShapeType.No_shape:
                return True
        return False

    def timerEvent(self, e):
        if e.timerId() == self.timer.timerId():
            # time.sleep(1)
            if self.waiting_new_shape:
                self.waiting_new_shape = False
                self.set_shape_in_boards()
                self.remove_full_lines()
            else:
                self.shape_down1line(0, 1)
        else:
            return super(Board, self).timerEvent(e)

    def shape_down1line(self, x_offset, y_offset):
        # shape 往下移动一行
        res = self.move_shape(self.cur_shape, x_offset, y_offset)
        # if res is False:
        #     self.set_shape_in_boards()
        #     self.remove_full_lines()
        return res

    def shape_drop_down(self):
        # 直接移动到底部
        while self.shape_down1line(0, 1):
            pass

    def shape_pause(self):
        if self.is_paused:
            self.timer.start(SPEED, self)
            self.msg2status_bar.emit("分数：" + str(self.num_lines_removed))
        else:
            self.timer.stop()
            self.msg2status_bar.emit("暂停")

        self.is_paused = not self.is_paused
        self.update()

    def keyPressEvent(self, event):
        key = event.key()
        
        if not self.game_start:
            return super(Board, self).keyPressEvent(event)
        if self.is_paused and key != Qt.Key_P:
            return super(Board, self).keyPressEvent(event)

        if key == Qt.Key_Up:
            # 上：左转
            self.move_shape(self.cur_shape.rotate_left(), 0, 0)
        elif key == Qt.Key_Down:
            # 下：右转
            self.move_shape(self.cur_shape.rotate_right(), 0, 0)
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
        else:
            return super(Board, self).keyPressEvent(event)

    def move_shape(self, shape, x_offset, y_offset):
        for i in range(len(shape.coors)):
            x = shape.get_x(i) + self.cur_x
            y = -shape.get_y(i) + self.cur_y

            if x + x_offset < 0 or x + x_offset >= WIDTH_GRID or y > HEIGHT_GRID-1:
                # 设定不能超出边界
                return None
            if y < 0:
                continue
            # if y == HEIGHT_GRID - 1:
            #     # 接触到了下边界
            #     self.set_shape_in_boards()
            #     self.remove_full_lines()
            #     pass
            if y == HEIGHT_GRID - 1 or self.boards[self.get_index_in_boards(x, y+1)] != ShapeType.No_shape:
                # 接触到了下边界 或 如果 x y 这个坐标在 boards 中不是空形状，返回 False
                self.waiting_new_shape = True
                return False

        self.cur_x += x_offset
        self.cur_y += y_offset
        self.cur_shape = shape
        self.update()
        return True

    def remove_full_lines(self):
        # 删除所有满行
        lines = list(set([self.cur_y - self.cur_shape.get_y(i) for i in range(len(self.cur_shape.coors))]))
        remove_lines = []

        for line in lines:
            for i in range(line*WIDTH_GRID, line*WIDTH_GRID+WIDTH_GRID):
                if self.boards[i] == ShapeType.No_shape:
                    break
            else:
                remove_lines.append(line)

        if remove_lines:
            remove_lines.sort()
            for remove_line in remove_lines:
                while remove_line > 0:
                    for i in range(remove_line*WIDTH_GRID, remove_line*WIDTH_GRID+WIDTH_GRID):
                        self.boards[i] = self.boards[i-WIDTH_GRID]
                    remove_line -= 1

        if len(remove_lines) > 0:
            self.num_lines_removed += len(remove_lines)
            self.msg2status_bar.emit("分数：" + str(self.num_lines_removed))

        self.new_shape()

    def get_shape_in_boards(self, x, y):
        return self.boards[self.get_index_in_boards(x, y)]

    def set_shape_in_boards(self):
        for i in range(len(self.cur_shape.coors)):
            x = self.cur_shape.get_x(i) + self.cur_x
            y = -self.cur_shape.get_y(i) + self.cur_y
            if y < 0 or x < 0:
                continue
            self.set_boards_shape_type(x, y, self.cur_shape.shape_type)

    def set_boards_shape_type(self, x, y, shape_type):
        count = self.get_index_in_boards(x, y)
        self.boards[count] = shape_type

    @classmethod
    def get_index_in_boards(cls, x, y):
        return y * WIDTH_GRID + x

    def draw_shape(self):
        qp = QPainter()
        qp.begin(self)

        for i in range(len(self.cur_shape.coors)):
            if self.cur_shape.shape_type == ShapeType.No_shape:
                break
            self.painter_square(
                qp, self.cur_x + self.cur_shape.get_x(i), self.cur_y - self.cur_shape.get_y(i), 1, 1,
                self.cur_shape.shape_type)

        for i in range(WIDTH_GRID):
            for j in range(HEIGHT_GRID):
                shape_type = self.get_shape_in_boards(i, j)
                if shape_type != ShapeType.No_shape:
                    self.painter_square(qp, i, j, 1, 1, shape_type)

        qp.end()

    def every_square_per_width(self):
        return self.contentsRect().width() // WIDTH_GRID

    def every_square_per_height(self):
        return self.contentsRect().height() // HEIGHT_GRID

    def painter_square(self, qp, x, y, width, height, shape_type):
        # 根据长宽和起始地点画框
        x *= self.every_square_per_width()
        y *= self.every_square_per_height()
        width *= self.every_square_per_width()
        height *= self.every_square_per_height()

        color = QColor(ShapeType.Shape_Colors[shape_type])
        qp.fillRect(x+1, y+1, width-1, height-2, color)

        qp.setPen(color.lighter())
        qp.drawLine(x, y, x+width-1, y)
        qp.drawLine(x, y, x, y+height-1)
        qp.setPen(color.darker())
        qp.drawLine(x+width-1, y+1, x+width-1, y+height-1)
        qp.drawLine(x+1, y+height-1, x+width-1, y+height-1)


class ShapeType:
    Shape_Colors = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC, 0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

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
        self.coors = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.shape_type = 0

    def set_random_shape(self):
        self.shape_type = random.randint(1, len(ShapeType.Coors_table)-1)
        return self.shape_type

    def set_shape_coors(self, shape_type):
        self.shape_type = shape_type
        for i in range(len(self.coors)):
            for j in range(len(self.coors[i])):
                self.coors[i][j] = ShapeType.Coors_table[shape_type][i][j]

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
        for i in range(len(self.coors)):
            shape.set_x(i, shape.get_x(i) + x_offset)
            shape.set_y(i, shape.get_y(i) + y_offset)
        return shape

    def rotate_left(self):
        # 向左旋转 90 度
        shape = Shape()
        shape.set_shape_coors(self.shape_type)
        for i in range(len(shape.coors)):
            shape.set_x(i, -self.get_y(i))
            shape.set_y(i, self.get_x(i))
        return shape

    def rotate_right(self):
        # 向右旋转 90 度
        shape = Shape()
        shape.set_shape_coors(self.shape_type)
        for i in range(len(shape.coors)):
            shape.set_x(i, self.get_y(i))
            shape.set_y(i, -self.get_x(i))
        return shape
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetris = Tetris()
    sys.exit(app.exec_())

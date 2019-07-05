import sys
import random

from PyQt5.QtCore import pyqtSignal, Qt, QBasicTimer
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFrame, QAction, QLabel, QVBoxLayout, QGridLayout,
    QWidget, QPushButton, QLCDNumber, QSlider
)


class Snake(QMainWindow):

    def __init__(self):
        super(Snake, self).__init__()

        self.setting = None
        self.board = None
        self.snake_dead_tips = None

        self.init_board()
        self.init_ui()

    def init_ui(self):

        menu = self.menuBar().addMenu('设置')
        menu.addAction(self.restart_action())
        menu.addAction(self.degree_of_difficulty_action())
        menu.addAction(self.pause_action())

        self.setGeometry(100, 100, 15*(Board.WIDTH+1), 15*(Board.HEIGHT+1)+45)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('贪吃蛇')
        self.show()

    def restart_action(self):
        restart_action = QAction(QIcon('./restart.jpg'), '&重新开始', self)
        restart_action.setShortcut('Ctrl+R')
        restart_action.triggered.connect(self.init_board)
        return restart_action

    def degree_of_difficulty_action(self):
        degree = QAction(QIcon('./setting.jpg'), '&设置速度', self)
        degree.setShortcut('Ctrl+Alt+S')
        degree.triggered.connect(self.init_setting)
        return degree
    
    def pause_action(self):
        pause = QAction(QIcon('./stop.jpg'), '&暂停', self)
        pause.setShortcut('Ctrl+Alt+T')
        pause.triggered.connect(self.board_paused)
        return pause

    def board_paused(self):
        self.board.paused()

    def init_board(self):
        # 界面
        Board.SPEED = Board.BASE_SPEED
        self.statusBar().showMessage("欢迎进入贪吃蛇")
        self.board = Board(self)

        self.board.msg2status_bar[str].connect(self.statusBar().showMessage)
        self.board.snake_dead_tips[str].connect(self.init_snake_dead_tips)

        self.setCentralWidget(self.board)
        self.board.setFocusPolicy(Qt.StrongFocus)
        self.board.setStyleSheet('QFrame { background-color: #dedede }')
        self.board.start()

    def init_setting(self):
        # 点击设置难度时显示的框
        self.board.paused()
        if self.setting:
            self.setting.show()
            return
        self.setting = Setting()
        x = self.geometry().left() + self.geometry().width()//2 - self.setting.contentsRect().width()//2
        y = self.geometry().top() + self.geometry().height()//2 - self.setting.contentsRect().height()//2 - 20
        self.setting.move(x, y)
        self.setting.show()
        self.setting.confirm.clicked.connect(self.setting.hide)
        self.setting.confirm.clicked.connect(self.setting_speed)

    def setting_speed(self):
        Board.SPEED = Board.BASE_SPEED - self.setting.value*2
        if Board.SPEED < 50:
            Board.SPEED = 50
        # self.board.depaused()

    def init_snake_dead_tips(self, msg):
        # 蛇死亡时显示确认框
        self.snake_dead_tips = SnakeDeadTips(msg)
        x = self.geometry().left() + self.geometry().width()//2 - self.snake_dead_tips.contentsRect().width()//2
        y = self.geometry().top() + self.geometry().height()//2 - self.snake_dead_tips.contentsRect().height()//2 - 20
        self.snake_dead_tips.move(x, y)
        self.snake_dead_tips.show()
        self.snake_dead_tips.ok.clicked.connect(self.init_board)
        self.snake_dead_tips.cancel.clicked.connect(self.close)


class Setting(QWidget):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super(Setting, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.confirm = QPushButton('确认')
        self.confirm.clicked.connect(self.close)

        lcd = QLCDNumber(self)  # 一个控件，该空间用于显示一个带有类似液晶显示屏效果的数字
        self.sld = QSlider(Qt.Horizontal, self)  # 滚动条

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(self.sld)
        vbox.addWidget(self.confirm)

        self.setLayout(vbox)
        self.sld.valueChanged.connect(lcd.display)  # 将滚动条的 valueChanged 信号连接到 lcd 的 display 插槽

        self.resize(15 * (Board.WIDTH // 2), 15 * (Board.HEIGHT // 2))
        self.setWindowIcon(QIcon("./01.jpg"))
        self.setWindowTitle('设置难度')
        self.show()

    @property
    def value(self):
        return self.sld.value()


class SnakeDeadTips(QWidget):

    def __init__(self, msg):
        super(SnakeDeadTips, self).__init__()
        self.msg = msg
        self.init_ui()

    def init_ui(self):

        tips = QLabel(self.msg)
        tips.setFont(QFont('SansSerif', 10))

        self.ok = QPushButton('确认')
        self.ok.clicked.connect(self.close)
        self.cancel = QPushButton('退出')
        self.cancel.clicked.connect(self.close)

        grid = QGridLayout()
        grid.addWidget(self.ok, 0, 0)
        grid.addWidget(self.cancel, 0, 1)

        vbox = QVBoxLayout()
        vbox.addWidget(tips)
        vbox.addLayout(grid)

        self.setLayout(vbox)
        self.resize(15*(Board.WIDTH//2), 15*(Board.HEIGHT//2))
        self.show()


class Board(QFrame):

    msg2status_bar = pyqtSignal(str)
    snake_dead_tips = pyqtSignal(str)

    BASE_SPEED = 250
    SPEED = 250
    WIDTH = 20
    HEIGHT = 20
    GAME_OVER_MSG = 'GAME OVER 重新来过？'

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.is_paused = False
        self.game_over = False

        self.timer = QBasicTimer()
        self.snake = SnakeNode()

    def start(self):
        self.timer.start(self.SPEED, self)
        self.paused()

    def timerEvent(self, e):
        if e.timerId() != self.timer.timerId():
            return super(Board, self).timerEvent(e)
        if self.snake.waiting_new_star:
            self.msg2status_bar.emit('score: %d' % len(self.snake.nodes))
            self.snake.waiting_new_star = False
            self.snake.set_new_star()
        self.snake_walk()

    def keyPressEvent(self, event):
        key = event.key()

        if self.is_paused and key != Qt.Key_P:
            return

        if key == Qt.Key_Up:
            self.snake.set_direct_up()
        elif key == Qt.Key_Down:
            self.snake.set_direct_down()
        elif key == Qt.Key_Left:
            self.snake.set_direct_left()
        elif key == Qt.Key_Right:
            self.snake.set_direct_right()
        elif key == Qt.Key_P:
            self.toggle_pause()
        else:
            return super(Board, self).keyPressEvent(event)

    def toggle_pause(self):
        if not self.is_paused:
            self.paused()
        else:
            self.depaused()

    def paused(self):
        self.timer.stop()
        self.msg2status_bar.emit('暂停( p 继续 )')
        self.is_paused = True

    def depaused(self):
        self.timer.start(self.SPEED, self)
        self.msg2status_bar.emit('score: %d' % len(self.snake.nodes))
        self.is_paused = False

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_snake(qp)
        self.draw_star(qp)
        qp.end()

    def snake_walk(self):
        # 蛇每次走一步
        if not self.snake.walk():
            self.snake_dead_tips.emit(self.GAME_OVER_MSG)
            self.msg2status_bar.emit('Game Over')
            self.timer.stop()
        self.update()

    def draw_snake(self, qp):
        head_x, head_y = self.snake.nodes[0]
        self.draw_cube(qp, head_x, head_y, SnakeNode.HEADER_COLOR)

        for x, y in self.snake.nodes[1:]:
            self.draw_cube(qp, x, y, SnakeNode.BODY_COLOR)

    def draw_star(self, qp):
        self.draw_cube(qp, self.snake.star_x, self.snake.star_y, SnakeNode.STAR_COLOR)

    def draw_cube(self, qp, x, y, color):
        color = QColor(color)

        width = self.board_cube_width()
        height = self.board_cube_height()
        x *= width
        y *= height

        qp.fillRect(x+1, y+1, width-2, height-2, color)

        qp.setPen(color.lighter())
        qp.setPen(color.darker())

    def board_cube_width(self):
        return 15
        return self.contentsRect().width() // self.WIDTH

    def board_cube_height(self):
        return 15
        return self.contentsRect().height() // self.HEIGHT


class SnakeNode(object):

    BODY_COLOR = '#00f'
    STAR_COLOR = '#000'
    HEADER_COLOR = '#f00'

    def __init__(self):

        self.star_x = -1
        self.star_y = -1
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

    def set_direct_up(self):
        if self.direct_x == 0 and self.direct_y == 1:
            return
        self.direct_x = 0
        self.direct_y = -1

    def set_direct_down(self):
        if self.direct_x == 0 and self.direct_y == -1:
            return
        self.direct_x = 0
        self.direct_y = 1

    def set_direct_left(self):
        if self.direct_x == 1 and self.direct_y == 0:
            return
        self.direct_x = -1
        self.direct_y = 0

    def set_direct_right(self):
        if self.direct_x == -1 and self.direct_y == 0:
            return
        self.direct_x = 1
        self.direct_y = 0

    @staticmethod
    def coordinate2int(x, y):
        return y*Board.WIDTH + x

    def set_new_star(self):
        x = random.randint(0, Board.WIDTH - 1)
        y = random.randint(0, Board.HEIGHT - 1)
        if self.coordinate_in_nodes_set(x, y):
            return self.set_new_star()
        else:
            self.star_x, self.star_y = x, y

    def walk(self):
        head_x = self.nodes[0][0]
        head_y = self.nodes[0][1]

        x = head_x + self.direct_x
        y = head_y + self.direct_y

        if self.coordinate_in_nodes_set(x, y):
            # 撞到了自己
            return False

        if x < 0 or x > Board.WIDTH or y < 0 or y > Board.HEIGHT:
            # 撞到了边界
            return False

        self.add2head(x, y)
        if x == self.star_x and y == self.star_y:
            self.waiting_new_star = True
            self.star_x = -1
            self.star_y = -1
            return True

        self.remove_tail()
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    snake = Snake()
    sys.exit(app.exec_())

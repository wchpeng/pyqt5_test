import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        cb = QCheckBox('显示标题', self)
        cb.move(30, 30)
        cb.stateChanged.connect(self.change_title)  # 复选框状态改变
        cb.toggle()  # 切换复选框状态（默认是不开启的，切换到开启，并且会触发上面绑定的方法）

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()

    def change_title(self, state):
        # state 是复选框的状态
        if state == Qt.Checked:
            self.setWindowTitle('复选框 check box')
        else:
            self.setWindowTitle(' ')  # 空如果用 '' 则会导致标题为默认值（默认值为 python3 ）


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

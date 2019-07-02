import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(20, 40, 200, 25)

        self.btn = QPushButton('start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.do_action)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('进度条')
        self.show()

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('finished')
            return

        self.step += 1
        self.pbar.setVal(self.step)

    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('start')
        else:
            self.timer.start(100, self)
            self.btn.setText('stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

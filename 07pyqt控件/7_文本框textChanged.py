import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QWidget


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        qle = QLineEdit(self)
        qle.move(20, 10)
        qle.textChanged[str].connect(self.line_edit007_change)

        self.lab = QLabel('test', self)
        self.lab.move(20, 50)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('文本框文本改变事件')
        self.show()

    def line_edit007_change(self, s):
        self.lab.setText(s)
        self.lab.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

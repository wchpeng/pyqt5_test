# 使用框显示一个回复框
import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout)
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        title = QLabel('标题')
        author = QLabel('作者')
        review = QLabel('回复')
        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(15)
        grid.addWidget(title, 0, 0)
        grid.addWidget(title_edit, 0, 1)
        grid.addWidget(author, 1, 0)
        grid.addWidget(author_edit, 1, 1)
        grid.addWidget(review, 2, 0)
        grid.addWidget(review_edit, 2, 1, 5, 1)

        self.setLayout(grid)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('回复')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




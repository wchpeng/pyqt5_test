import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QTextEdit, QGridLayout


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        title = QLabel('title')
        author = QLabel('Author')
        review = QLabel('review')

        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)  # 是指每行和每列的间距（表单中各组件的间距）

        grid.addWidget(title, 0, 0)
        grid.addWidget(author, 1, 0)
        grid.addWidget(review, 2, 0)

        grid.addWidget(title_edit, 0, 1)
        grid.addWidget(author_edit, 1, 1)
        grid.addWidget(review_edit, 2, 1, 5, 1)  # 5以上才会 review 在第一行，为什么？

        self.setLayout(grid)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('grid input label')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

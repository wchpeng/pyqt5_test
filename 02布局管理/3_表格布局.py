import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = [
            'cls', 'bck', '', 'close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]  # 表格中每个按钮的名字
        positions = [(i, j) for i in range(5) for j in range(4)]  # 表格中位置的列表

        for position, name in zip(positions, names):
            if name == '':
                continue
            btn = QPushButton(name)
            grid.addWidget(btn, *position)  # 把按钮放到表格的指定位置

        # self.setGeometry(100, 100, 300, 300)
        self.resize(300, 150)
        self.move(300, 150)

        self.setWindowTitle('表格布局 grid calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  # app.exec_() 是执行这个应用，必须有，否则显示无效

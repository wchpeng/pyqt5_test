import sys

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # self.resize(350, 350)
        self.setGeometry(0, 0, 350, 350)

        self.center()  # 将界面放到屏幕中间，没这个， resize 默认就是中间, setGeometry 默认不是中心

        self.setWindowTitle('显示中心 Center')
        self.show()

    def center(self):
        # 控制窗口显示在屏幕中心

        # 获得屏幕
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()

        print("-------------------------------")
        print("before qr: ", qr)
        qr.moveCenter(cp)
        # 显示到屏幕中心
        print("cp: ", cp)
        print("after qr: ", qr)
        print("-------------------------------")
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

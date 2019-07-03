import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap('./openfile.png')

        lab = QLabel(self)
        lab.setPixmap(pixmap)

        hbox.addWidget(lab)
        self.setLayout(hbox)

        self.setGeometry(100, 100, 100, 100)  # 如果图标太大，会自动放大界面
        # self.move(300, 300)
        self.setWindowTitle('图像控件')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

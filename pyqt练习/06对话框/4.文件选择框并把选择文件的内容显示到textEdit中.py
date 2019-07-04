import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QFileDialog, QAction


class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.text = QTextEdit()
        self.setCentralWidget(self.text)

        file_action = QAction(QIcon('openfile.png'), '打开文件', self)
        file_action.setShortcut('Ctrl+O')
        file_action.triggered.connect(self.show_file_dialog)

        self.statusBar()
        menu1 = self.menuBar().addMenu('文件')
        menu1.addAction(file_action)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('文件选择')
        self.setWindowIcon(QIcon('./01.jpg'))
        self.show()

    def show_file_dialog(self, event):
        print("打开文件")
        # 后面的 "TXT Files(*.txt)" 表示只打开 txt 文件，多个规则可用 ;; 分割
        # 如："TXT Files(*.txt);;Image Files(*.png)"
        frame = QFileDialog.getOpenFileName(
            self, "打开文件007", "C:\\Users\\sm\\Desktop", "TXT Files(*.txt)"
        )

        if frame:
            with open(frame[0], 'r') as f:
                content = f.read()
                self.text.setText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

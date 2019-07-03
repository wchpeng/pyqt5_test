import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):

        cal = QCalendarWidget(self)  # 创建日历控件
        cal.setGridVisible(True)  # 这个方法让每天的日期中间出现网格
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.show_date)  # 点击日期发出信号，给 show_date 方法

        self.lab = QLabel(self)
        self.lab.move(30, 230)

        # 下面三行是获取当前日期并赋值给 lab，如果没有这两行，lab 初始为空，再赋值时就会出现长度不够显示的问题
        # 就算是这样也会出现那个问题，因为月份和号数有单有双
        date = cal.selectedDate()
        date_str = date.toString().ljust(17)  #这里如果不转化为 17 个字符，当月份和号数都为双数时会显示不全，如：12月25日
        self.lab.setText(date_str)

        self.setGeometry(100, 100, 360, 300)
        self.setWindowIcon(QIcon('./01.jpg'))
        self.setWindowTitle('日历控件')
        self.show()

    def show_date(self, date):
        # date 是 PyQt5.QtCore.QDate 类型的数据，toString 转化为字符串
        self.lab.setText(date.toString().ljust(17))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

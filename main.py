import io
import sys

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from random import randint


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        # f = io.StringIO(template)
        uic.loadUi("Ui.ui", self)
        self.setGeometry(300, 300, 450, 450)
        self.flag = False
        self.pushButton.clicked.connect(self.draw_flag)

    def draw_flag(self):
        # Создаем объект QPainter для рисования
        # qp = QPainter()
        # Начинаем процесс рисования
        self.flag = True
        # qp.begin(self)

        # qp.end()
        self.update()


    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            qp.begin(self)
            x, y = [randint(10, 500) for i in range(2)]
            d = randint(10, 500)

            # qp.setBrush(QColor(*[randint(0, 255) for i in range(3)]))
            qp.setBrush(QColor(255,255,0))
            qp.drawEllipse(x, y, d, d)
            self.Flag = False
            qp.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())








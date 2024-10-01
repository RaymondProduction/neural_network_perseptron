import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QPoint

from calc import MatrixManipulation

from mainwindow import Ui_MainWindow

matrixManipulator = MatrixManipulation()

class PaintWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.figures = []  # Список для зберігання всіх фігур (ліній)
        self.current_points = []  # Точки для поточної фігури

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.current_points = [event.pos()]  # Початок нової фігури
            # print(" mousePressEvent > ", event.pos())
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.current_points.append(event.pos())  # Додаємо нову точку до поточної фігури
            print(" mouseMoveEvent > ", event.pos().x())
            matrixManipulator.put_val(event.pos(), 5)
            matrixManipulator.show()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.figures.append(self.current_points)  # Додаємо поточну фігуру до списку всіх фігур
            self.current_points = []

    def paintEvent(self, event):
        painter = QPainter(self)

        # Фон для віджета
        painter.fillRect(self.rect(), Qt.GlobalColor.white)

        # Налаштування пензля для малювання
        pen = QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
        painter.setPen(pen)

        # Малюємо всі збережені фігури
        for points in self.figures:
            if len(points) > 1:
                for i in range(len(points) - 1):
                    painter.drawLine(points[i], points[i + 1])

        # Малюємо поточну фігуру
        if len(self.current_points) > 1:
            for i in range(len(self.current_points) - 1):
                painter.drawLine(self.current_points[i], self.current_points[i + 1])

    # def setGeometry(self, geometry):
    #     super().setGeometry(geometry)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Замінюємо звичайний віджет на PaintWidget
        self.paint_widget = PaintWidget(self.ui.centralwidget)
        self.paint_widget.setGeometry(self.ui.widget.geometry())
        self.paint_widget.setObjectName("paint_widget")


        # Видаляємо попередній простий віджет
        self.ui.widget.deleteLater()
        self.ui.widget = self.paint_widget

        matrixManipulator.set_geometry(self.ui.widget.geometry())
        matrixManipulator.create(lambda : 0)
        matrixManipulator.show()


        self.ui.clearButton.clicked.connect(lambda:
                                            matrixManipulator.create(lambda : 0)
                                            )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

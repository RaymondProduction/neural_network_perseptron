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
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.current_points.append(event.pos())  # Додаємо нову точку до поточної фігури
            matrixManipulator.put_val(event.pos(), 1)
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

    def draw_from_matrix(self, matrix):
        # Очищаємо фігури перед малюванням нових
        self.figures = []

        cell_width = self.width() // 20
        cell_height = self.height() // 20

        # Створюємо фігури на основі даних у матриці
        for i in range(20):
            for j in range(20):
                if matrix[i][j] == 1:
                    x = i * cell_width
                    y = j * cell_height
                    # Малюємо невеликий квадрат на основі матриці
                    self.figures.append([QPoint(x, y), QPoint(x + cell_width, y + cell_height)])

        # Оновлюємо віджет для відображення змін
        self.update()

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
        matrixManipulator.create(lambda: 0)
        matrixManipulator.show()

        self.ui.clearButton.clicked.connect(self.clear_all)
        self.ui.alignButton.clicked.connect(self.align)

    def clear_all(self):
        # Очищаємо всі фігури і матрицю
        self.paint_widget.figures = []
        self.paint_widget.current_points = []
        matrixManipulator.create(lambda: 0)
        self.paint_widget.update()  # Оновлюємо віджет для очищення екрана

    def align(self):
        # Вирівнюємо матрицю і оновлюємо зображення відповідно до нових даних
        matrixManipulator.align()
        self.paint_widget.draw_from_matrix(matrixManipulator.matrix)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

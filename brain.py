import random

from PyQt6.QtWidgets import QMessageBox


class Brain:
    def __init__(self):
        self.weights = []
        self.random_weights()
        self.speed = 0.7

    def perseptron(self, matrix):
        sum = 0 # вхід персептрона
        #rety = None # зенайдений вихід персептрона
        #test = None # напрямок корегування ваг

        print("matrix ", matrix)
        print("weights ", self.weights)

        for i in range(20):
            for j in range(20):
                sum+=matrix[i][j]*self.weights[i][j]

        if sum > 0:
            rety = 1
        else:
            rety = 0

        # Створюємо QMessageBox з питанням залежно від значення rety
        if rety == 1:
            text = "X?"
        else:
            text = "O?"

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Question")
        msg_box.setText(text)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # Отримуємо відповідь від користувача
        reply = msg_box.exec()

        if reply == QMessageBox.StandardButton.No:
            if rety == 0:
                test = 1
            else:
                test = -1
            for i in range(20):
                for j in range(20):
                    self.weights[i][j] = self.weights[i][j] + self.speed*test*matrix[i][j]

    def random_weights(self):
        for i in range(20):
            row = []
            for j in range(20):
                row.append((-3 + random.randint(0, 5)) / 10.0)
            self.weights.append(row)



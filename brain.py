import random

from PyQt6.QtWidgets import QMessageBox


class Brain:
    def __init__(self, square_size):
        self.square_size = square_size
        self.weights = []
        self.random_weights()
        self.speed = 0.7

    def perseptron(self, matrix):
        total_sum = 0 # вхід персептрона
        #rety = None # зенайдений вихід персептрона
        #test = None # напрямок корегування ваг

        print("matrix ", matrix)
        print("weights ", self.weights)

        for i in range(self.square_size):
            for j in range(self.square_size):
                total_sum+= matrix[i][j] * self.weights[i][j]

        if total_sum > 0:
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
            for i in range(self.square_size):
                for j in range(self.square_size):
                    self.weights[i][j] = self.weights[i][j] + self.speed*test*matrix[i][j]

    def random_weights(self):
        for i in range(self.square_size):
            row = []
            for j in range(self.square_size):
                row.append((-3 + random.randint(0, 5)) / 10.0)
            self.weights.append(row)


    def save_weights(self):
        with open("weights.dat", "w") as file:
            for j in range(self.square_size):
                for i in range(self.square_size):
                    file.write(f"{self.weights[i][j]}\t")  # Записуємо вагу з табуляцією
                file.write("\n")  # Новий рядок після кожного рядка ваг




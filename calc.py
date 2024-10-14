import os


class MatrixManipulation:
    def __init__(self, size):
        self.matrix = []
        self.width_px = None
        self.height_px = None
        self.size = size

    def align(self):
        tmp = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            tmp.append(row)

        x_min = self.size
        x_max = -1
        y_min = self.size
        y_max = -1

        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == 1:
                    if i < x_min:
                        x_min = i
                    if i > x_max:
                        x_max = i
                    if j < y_min:
                        y_min = j
                    if j > y_max:
                        y_max = j

        print(f"x_min={x_min} x_max = {x_max}")

        for i in range(self.size):
            for j in range(self.size):
                xx = i/self.size * (x_max - x_min +1)
                yy = j/self.size * (y_max - y_min +1)
                tmp[i][j] = self.matrix[x_min + int(xx)][y_min + int(yy)]

        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = tmp[i][j]

    def create(self, fill_value):
        self.matrix = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(fill_value())
            self.matrix.append(row)

        return self

    def clear(self, matrix):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[j][i] = 0
        return  self

    @staticmethod
    def clear_console():
        # Перевіряємо, на якій платформі виконується код
        if os.name == 'nt':  # Якщо Windows
            os.system('cls')
        else:  # Якщо Linux або MacOS
            os.system('clear')

    def put_val(self, pos, value):
        x = pos.x()
        y = pos.y()
        i = x * self.size // self.width_px
        j = y * self.size // self.height_px

        if 0 <= i < self.size and 0 <= j < self.size:
            self.matrix[i][j] = value

        return self

    def set_geometry(self, geometry):
        self.width_px = geometry.width()
        self.height_px = geometry.height()

    def show(self):
        self.clear_console()
        for row in self.matrix:
            print(row, sep="\n")


class MatrixManipulation:
    def __init__(self):
        self.matrix = []
        self.width_px = None
        self.height_px = None

    def align(self):
        tmp = []
        for i in range(20):
            row = []
            for j in range(20):
                row.append(0)
            tmp.append(row)

        x_min = 20
        x_max = -1
        y_min = 20
        y_max = -1

        for i in range(20):
            for j in range(20):
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

        for i in range(20):
            for j in range(20):
                xx = i/20 * (x_max - x_min +1)
                yy = j/20 * (y_max - y_min +1)
                tmp[i][j] = self.matrix[x_min + int(xx)][y_min + int(yy)]

        for i in range(20):
            for j in range(20):
                self.matrix[i][j] = tmp[i][j]

    def create(self, fill_value):
        self.matrix = []
        for i in range(20):
            row = []
            for j in range(20):
                row.append(fill_value())
            self.matrix.append(row)

        return self

    def clear(self, matrix):
        for i in range(20):
            for j in range(20):
                self.matrix[j][i] = 0
        return  self

    def put_val(self, pos, value):
        x = pos.x()
        y = pos.y()
        i = x * 20 // self.width_px
        j = y * 20 // self.height_px

        if 0 <= i < 20 and 0 <= j < 20:
            self.matrix[i][j] = value

        return self

    def set_geometry(self, geometry):
        self.width_px = geometry.width()
        self.height_px = geometry.height()

    def show(self):
        for row in self.matrix:
            print(row)

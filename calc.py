
class MatrixManipulation:
    def __init__(self):
        self.matrix = []
        self.width_px = None
        self.height_px = None

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

class Mapping:
    pass


class LinearTo2DArray(Mapping):
    def __init__(self, length, width, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.length = length
        self.width = width

    def map_linear_2D(self, idx):
        return idx % self.width, idx // self.width

    def map_2D_linear(self, x, y):
        return int(x + self.width * y)

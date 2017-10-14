class Vector:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 1.0

    @property
    def values(self):
        return self.x, self.y, self.z, self.w

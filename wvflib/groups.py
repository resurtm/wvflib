class SmoothGroup:
    def __init__(self):
        self.name = ''
        self.faces = []

    @property
    def empty(self):
        return len(self.faces) == 0


class Group:
    def __init__(self):
        self.name = ''
        self.smooth_groups = []
        self.faces = []
        self.material = None

    @property
    def empty(self):
        return len(self.faces) == 0

class SmoothGroup:
    def __init__(self):
        self.name = ''
        self.faces = []


class Group:
    def __init__(self):
        self.name = ''
        self.smooth_groups = []
        self.faces = []
        self.material = None

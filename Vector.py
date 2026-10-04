class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getPos(self):
        return (self.x, self.y)
    def updateX(self, amount):
        self.x += amount
    def updateY(self, amount):
        self.y += amount
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return Vector(self.x, self.y)
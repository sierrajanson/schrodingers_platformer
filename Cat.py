from Vector import Vector
class Cat:
    def __init__(self, animation, pos, velocity, hitbox):
        self.pos = pos
        self.hitbox = hitbox
        self.velocity = velocity
        self.animation = animation
        self.is_jumping = False
        self.start_y = None
        print(self.pos)
    def draw(self):
        self.animation.animate(self.pos.getPos(), 5, self.velocity)
    def goLeft(self):
        self.velocity.x = -1.5
    def goRight(self):
        self.velocity.x = 1.5
    def goUp(self):
        self.velocity.y = -1.5
    def goDown(self):
        self.velocity.y = 1.5
    def stayStill(self):
        self.velocity.x = 0
    def jump(self):
        if not self.is_jumping:
            self.start_y = self.pos.y
            self.velocity.y = -12
        self.is_jumping = True
    def move(self):
        if self.velocity.y < 0:
            self.velocity += Vector(0, 0.5)
        elif self.start_y and self.pos.y < self.start_y:
            self.velocity += Vector(0, 0.5)
            # move to collision
        elif self.start_y and self.pos.y >= self.start_y:
            self.is_jumping = False
            self.velocity.y = 0     
        self.pos += self.velocity
        self.hitbox.position = self.pos

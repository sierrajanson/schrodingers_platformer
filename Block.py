class Block:
    def __init__(self, animation, position, velocity, hitbox):
        self.animation = animation
        self.pos = position
        self.min_y = position.y + 2
        self.max_y = position.y - 2
        self.velocity = velocity
        self.hitbox = hitbox
    def draw(self):
        self.animation.animate(self.pos.getPos(), 1, self.velocity)
    def move(self):
        if self.pos.y < self.max_y:
            self.velocity.y = 0.05
        if self.pos.y > self.min_y:
            self.velocity.y = -0.05
        self.pos.y += self.velocity.y
        self.hitbox.position = self.pos
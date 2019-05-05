import random

class Blob:
    """basic pygame class"""

    def __init__(self, color, x_boundary, y_boundary, movement_range):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.color = color
        self.size = random.randrange(4, 8)
        self.movement_range = movement_range

    def move(self):
        self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 5:
            self.x = 5
        elif self.x > self.x_boundary - 5:
            self.x = self.x_boundary - 50
            print("gotchaX")

        if self.y < 5:
            self.y = 50
        elif self.y > self.y_boundary - 5:
            self.y = self.y_boundary - 50
            print("gotchaY")

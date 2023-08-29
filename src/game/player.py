import pygame


class Player():
    def __init__(self, size, x, y, color):
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.step_size = 2

    def draw(self,screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.size)

    def compute_player_move(self, input):
        x = self.x
        y = self.y
        step = self.step_size
        if input.is_diag():
            step *= .75
        if input.up:
            y -= step
        if input.down:
            y += step
        if input.left:
            x -= step
        if input.right:
            x += step
        return x,y

    def move_player(self, x , y):
        self.x = x
        self.y = y

    def get_player_boundaries(self, x = None, y = None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        return (x-self.size, y-self.size, x+self.size, y+self.size)

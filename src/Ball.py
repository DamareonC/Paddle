import random
import pygame


class Ball:
    rect = pygame.Rect(320, 320, 10, 10)

    def __init__(self):
        self.x_speed = 3 if random.randint(1, 2) == 1 else -3  # Makes the ball have a 50% chance to go either left or right when the game starts
        self.y_speed = 3

    # Changes the vertical speed of the ball
    def change_speed(self):
        if self.y_speed > 0:
            self.y_speed = random.randint(4, 6)
        if self.y_speed < 0:
            self.y_speed = -random.randint(4, 6)

    # Redirects the ball and changes the vertical speed
    def on_hit(self):
        if random.randint(1, 4) == 1:  # Each hit has a 25% chance to slightly increase horizontal ball speed
            self.x_speed = self.x_speed + 0.1 if self.x_speed > 0 else self.x_speed - 0.1
        if self.x_speed < 0:
            self.x_speed = -self.x_speed
            self.change_speed()
        elif self.x_speed > 0:
            self.x_speed = -self.x_speed
            self.change_speed()

    # Moves the ball within screen bounds
    def move(self):
        if self.rect.top <= 0:
            self.y_speed = abs(self.y_speed)
        if self.rect.bottom >= 639:
            self.y_speed = -self.y_speed

        self.rect.move_ip(self.x_speed, self.y_speed)

    def update(self):
        self.move()

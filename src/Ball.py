import random
import pygame


class Ball:
    rect: pygame.Rect = pygame.Rect(320, 320, 10, 10)

    def __init__(self) -> None:
        self.x_speed: int = 3 if random.randint(a=1, b=2) == 1 else -3  # Makes the ball have a 50% chance to go either left or right when the game starts
        self.y_speed: int = 3

    # Changes the vertical speed of the ball
    def change_speed(self) -> None:
        if self.y_speed > 0:
            self.y_speed = random.randint(a=4, b=6)
        if self.y_speed < 0:
            self.y_speed = -random.randint(a=4, b=6)

    # Redirects the ball and changes the vertical speed
    def on_hit(self) -> None:
        if random.randint(a=1, b=4) == 1:  # Each hit has a 25% chance to slightly increase horizontal ball speed
            self.x_speed = self.x_speed + 0.1 if self.x_speed > 0 else self.x_speed - 0.1
        if self.x_speed < 0:
            self.x_speed = -self.x_speed
            self.change_speed()
        elif self.x_speed > 0:
            self.x_speed = -self.x_speed
            self.change_speed()

    # Moves the ball within screen bounds
    def move(self) -> None:
        if self.rect.top <= 0:
            self.y_speed = abs(__x=self.y_speed)
        if self.rect.bottom >= 639:
            self.y_speed = -self.y_speed

        self.rect.move_ip(self.x_speed, self.y_speed)

    def update(self) -> None:
        self.move()

import os
import random

from pygame import *
from pygame.mixer import Sound


class Ball:
    def __init__(self) -> None:
        self.rect: Rect = Rect(320, 320, 10, 10)
        self.bounce_sound: Sound = Sound(os.path.join(os.path.dirname(__file__), r"../res/sounds/bounce.ogg"))
        self.hit_sound: mixer.Sound = mixer.Sound(os.path.join(os.path.dirname(__file__), r"../res/sounds/hit.ogg"))

        self.x_speed: int = 3 if random.randint(a=1, b=2) == 1 else -3  # Makes the ball have a 50% chance to go either left or right when the game starts
        self.y_speed: int = 3

    # Changes the vertical speed of the ball
    def change_speed(self) -> None:
        self.y_speed = random.randint(a=4, b=6) if self.y_speed > 0 else -random.randint(a=4, b=6)

    # Redirects the ball and changes the vertical speed
    def on_hit(self) -> None:
        if random.randint(a=1, b=4) == 1:  # Each hit has a 25% chance to slightly increase horizontal ball speed
            self.x_speed = self.x_speed + 0.1 if self.x_speed > 0 else self.x_speed - 0.1

        self.hit_sound.play()
        self.x_speed = -self.x_speed
        self.change_speed()

    # Moves the ball within screen bounds
    def move(self) -> None:
        if self.rect.top <= 0 or self.rect.bottom >= 639:
            self.bounce_sound.play()
            self.y_speed = -self.y_speed

        self.rect.move_ip(self.x_speed, self.y_speed)

    def update(self) -> None:
        self.move()

    def get_rect(self) -> Rect:
        return self.rect

    def get_x_speed(self) -> int:
        return self.x_speed

    def reset_position(self) -> None:
        self.rect.right = 320
        self.rect.top = 320
        self.x_speed: int = 3 if random.randint(a=1, b=2) == 1 else -3
        self.y_speed: int = 3

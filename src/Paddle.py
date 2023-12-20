from pygame import *
from Ball import Ball

class PaddleOne:  # The Player's Paddle
    def __init__(self) -> None:
        self.rect: Rect = Rect(0, 320, 10, 60)  # Sets the paddle to pos (0, 320) and makes paddle 10px in width, 60px in height
        self.speed: float = 5.0
        self.score = 0

    def move(self) -> None:
        pressed_keys: [bool] = key.get_pressed()

        # Makes the paddle stay within screen bounds
        if self.rect.top >= 0:
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                self.rect.move_ip(0.0, -self.speed)
        if self.rect.bottom <= 640:
            if pressed_keys[K_DOWN] or pressed_keys[K_s]:
                self.rect.move_ip(0.0, self.speed)

    def hit(self, ball: Ball) -> None:
        if self.rect.colliderect(ball.get_rect()):  # True if the paddle hits the ball
            ball.on_hit()

    def update(self) -> None:
        self.move()

    def get_rect(self) -> Rect:
        return self.rect

    def reset_position(self) -> None:
        self.rect.right = 10
        self.rect.top = 320

class PaddleTwo:  # The AI's Paddle
    def __init__(self) -> None:
        self.rect: Rect = Rect(630, 320, 10, 60)
        self.speed: float = 5.0
        self.score = 0

    def move(self, ball: Ball) -> None:  # Makes the AI's paddle follow the ball and stay within screen bounds
        if ball.get_x_speed() > 0:  # Makes Paddle Two only move when the ball is going towards it
            if self.rect.top > 0:
                if self.rect.centery > ball.get_rect().centery:
                    self.rect.move_ip(0.0, -self.speed)
            if self.rect.bottom < 640:
                if self.rect.centery < ball.get_rect().centery:
                    self.rect.move_ip(0.0, self.speed)

    def hit(self, ball: Ball) -> None:
        if self.rect.colliderect(ball.get_rect()):
            ball.on_hit()

    def update(self, ball: Ball) -> None:
        self.move(ball=ball)

    def get_rect(self) -> Rect:
        return self.rect

    def reset_position(self) -> None:
        self.rect.right = 640
        self.rect.top = 320
import pygame
import Ball


class PaddleOne:  # The Player's Paddle
    def __init__(self):
        self.rect = pygame.Rect(0, 320, 10, 60)  # Sets the paddle to (0, 320) and makes paddle 10px in width, 60px in height
        self.speed = 5.0

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        # Makes the paddle stay within screen bounds
        if self.rect.top >= 0:
            if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
                self.rect.move_ip(0.0, -self.speed)
        if self.rect.bottom <= 640:
            if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
                self.rect.move_ip(0.0, self.speed)

    def hit(self, ball: Ball.Ball):
        if self.rect.colliderect(ball):  # True if the paddle hits the ball
            ball.on_hit()

    def update(self):
        self.move()


class PaddleTwo:  # The AI's Paddle
    def __init__(self):
        self.rect = pygame.Rect(630, 320, 10, 60)
        self.speed = 5.0

    def move(self, ball: Ball.Ball):  # Makes the AI's paddle follow the ball and stay within screen bounds
        if ball.x_speed > 0:  # Makes Paddle Two only move when the ball is going towards it
            if self.rect.top > 0:
                if self.rect.centery > ball.rect.centery:
                    self.rect.move_ip(0.0, -self.speed)
            if self.rect.bottom < 640:
                if self.rect.centery < ball.rect.centery:
                    self.rect.move_ip(0.0, self.speed)

    def hit(self, ball: Ball.Ball):
        if self.rect.colliderect(ball):
            ball.on_hit()

    def update(self, ball: Ball.Ball):
        self.move(ball)

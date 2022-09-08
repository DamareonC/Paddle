import sys
import pygame
import Paddle
import Ball


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((640, 640))
        pygame.display.set_caption("Paddle")
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.paddle_one = Paddle.PaddleOne()
        self.paddle_two = Paddle.PaddleTwo()
        self.ball = Ball.Ball()

        self.run()

    def update(self):
        self.paddle_one.update()
        self.paddle_two.update(self.ball)
        self.paddle_one.hit(self.ball)
        self.paddle_two.hit(self.ball)
        self.ball.update()

        pygame.display.update()

    def draw(self):
        self.window.fill((0, 0, 0))

        pygame.draw.rect(surface=self.window, rect=self.paddle_one.rect, color=(255, 255, 255))
        pygame.draw.rect(surface=self.window, rect=self.paddle_two.rect, color=(255, 255, 255))
        pygame.draw.rect(surface=self.window, rect=self.ball.rect, color=(255, 255, 255))

        self.clock.tick(self.FPS)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            if Ball.Ball.rect.left <= -20 or Ball.Ball.rect.right >= 660:  # Stops the program when a paddle scores. Will add score and win systems later.
                self.running = False
                pygame.quit()
                sys.exit()

            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

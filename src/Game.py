import os
import sys
import time
import pygame

from pygame import Surface, font, mixer
from Paddle import PaddleOne, PaddleTwo
from Ball import Ball


def is_colliding_point(point: tuple[int, int], rect_pos: tuple[int, int], rect_size: [int, int]):
    return rect_pos[0] <= point[0] <= rect_pos[0] + rect_size[0] and rect_pos[1] <= point[1] <= rect_pos[1] + rect_size[1]


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.window: Surface = pygame.display.set_mode(size=(640, 640))
        pygame.display.set_caption("Paddle")

        self.font: font.Font = font.Font(os.path.join(os.path.dirname(__file__), r"../res/fonts/courier.ttf"), 36)
        self.score_sound: mixer.Sound = mixer.Sound(os.path.join(os.path.dirname(__file__), r"../res/sounds/score.ogg"))

        self.title: Surface = self.font.render('Paddle', True, 'white')
        self.win: Surface = self.font.render('', True, 'white')
        self.start: Surface = self.font.render('Start', True, 'white')
        self.restart: Surface = self.font.render('Restart', True, 'white')
        self.exit: Surface = self.font.render('Exit', True, 'white')

        self.title_pos: tuple[int, int] = (320 - self.title.get_size()[0] // 2, 100)
        self.win_pos: tuple[int, int] = (320 - self.win.get_size()[0] // 2, 100)
        self.start_pos: tuple[int, int] = (320 - self.start.get_size()[0] // 2, 300)
        self.restart_pos: tuple[int, int] = (320 - self.restart.get_size()[0] // 2, 300)
        self.exit_pos: tuple[int, int] = (320 - self.exit.get_size()[0] // 2, 400)

        self.running: bool = True
        self.screen: int = 0  # 0 = start, 1 = playing, 2 = game over/restart
        self.winner: int = -1  # -1 = neither, 0 = player, 1 = opponent

        self.paddle_one: PaddleOne = PaddleOne()
        self.paddle_two: PaddleTwo = PaddleTwo()
        self.ball: Ball = Ball()

        self.run()

    def update(self) -> None:
        if self.screen == 1:
            self.paddle_one.update()
            self.paddle_two.update(ball=self.ball)
            self.paddle_one.hit(ball=self.ball)
            self.paddle_two.hit(ball=self.ball)
            self.ball.update()
            self.score()

        pygame.display.update()

    def draw(self) -> None:
        self.window.fill(color=(0, 0, 0))

        match self.screen:
            case 0: self.start_screen()
            case 1: self.game_screen()
            case 2: self.game_over_screen()

    def run(self) -> None:
        last_time: int = time.time_ns()
        ns_per_update: float = 1000000000.0 / 60.0  # 60 is the updates per second
        delta: float = 0

        while self.running:
            current_time: int = time.time_ns()

            delta += (current_time - last_time) / ns_per_update  # Delta is increased ns_per_update/(current_time - last_time) times before it reaches 1 (update). current_time - last_time is the time it took to complete one loop
            last_time = current_time

            while delta >= 1:  # Runs the loop if at least 1/60th the second (1 update) has gone by
                self.update()
                delta -= 1

            self.draw()

            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
                    case pygame.MOUSEBUTTONDOWN:
                        match self.screen:
                            case 0:
                                if is_colliding_point(event.pos, self.start_pos, self.start.get_size()):
                                    self.screen = 1
                            case 2:
                                if is_colliding_point(event.pos, self.restart_pos, self.restart.get_size()):
                                    self.screen = 1
                                    self.paddle_one.score = 0
                                    self.paddle_two.score = 0

                        if is_colliding_point(event.pos, self.exit_pos, self.exit.get_size()):
                            self.running = False

        pygame.quit()
        sys.exit()

    def score(self) -> None:
        if self.ball.get_rect().left <= -20:
            self.score_sound.play()
            self.paddle_two.score += 1

            if self.paddle_two.score == 5:
                self.winner = 1
                self.screen = 2
                self.win: Surface = self.font.render(('Player' if self.winner == 0 else 'CPU') + ' Wins!', True, 'white')
                self.win_pos: tuple[int, int] = (320 - self.win.get_size()[0] // 2, 100)

            self.reset()
        elif self.ball.get_rect().right >= 660:
            self.score_sound.play()
            self.paddle_one.score += 1

            if self.paddle_one.score == 5:
                self.winner = 0
                self.screen = 2
                self.win: Surface = self.font.render(('Player' if self.winner == 0 else 'CPU') + ' Wins!', True, 'white')
                self.win_pos: tuple[int, int] = (320 - self.win.get_size()[0] // 2, 100)

            self.reset()

    def reset(self) -> None:
        self.ball.reset_position()
        self.paddle_one.reset_position()
        self.paddle_two.reset_position()

    def game_screen(self):
        pygame.draw.rect(surface=self.window, rect=self.paddle_one.get_rect(), color=(255, 255, 255))
        pygame.draw.rect(surface=self.window, rect=self.paddle_two.get_rect(), color=(255, 255, 255))
        pygame.draw.rect(surface=self.window, rect=self.ball.get_rect(), color=(255, 255, 255))

        self.window.blit(self.font.render(self.paddle_one.score.__str__(), True, 'white'), (150, 0))
        self.window.blit(self.font.render(self.paddle_two.score.__str__(), True, 'white'), (470, 0))

    def start_screen(self) -> None:
        self.window.blit(self.title, self.title_pos)
        self.window.blit(self.start, self.start_pos)
        self.window.blit(self.exit, self.exit_pos)

    def game_over_screen(self) -> None:
        self.window.blit(self.win, self.win_pos)
        self.window.blit(self.restart, self.restart_pos)
        self.window.blit(self.exit, self.exit_pos)

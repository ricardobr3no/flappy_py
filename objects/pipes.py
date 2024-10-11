import pygame
from config import grupos
from random import randint

SPEED = 3


class Pipe(pygame.sprite.Sprite):
    def __init__(self, spawn_position: tuple) -> None:
        super().__init__()
        self.load(spawn_position)

    def load(self, spawn_position):
        self.image = pygame.Surface((40, 300))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = spawn_position

    def update(self, dt) -> None:
        self.rect.x -= SPEED
        if self.rect.x < -20:
            self.kill()


class Pontuador(pygame.sprite.Sprite):
    def __init__(self, spawn_position: tuple):
        super().__init__()
        self.load(spawn_position)

    def load(self, spawn_position: tuple):
        self.image = pygame.Surface((20, 110))
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = spawn_position

    def update(self, dt):
        self.rect.x -= SPEED
        if self.rect.x < -20:
            self.kill()


def instanciar_pipes():
    margin = 90
    pos_x, pos_y = 700, randint(200, 300)
    pipe_up = Pipe((pos_x, pos_y - margin))
    pipe_up.rect.y -= 230
    pipe_bottom = Pipe((pos_x, pos_y + margin))
    pontuador = Pontuador((pos_x + 40, pos_y - 20))
    grupos["pipes"].add(pipe_up, pipe_bottom)
    grupos["pontuador"].add(pontuador)

import pygame
from config import TELA

GRAVITY = 0.4


class Bird(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.load()

    def load(self):
        self.image = pygame.Surface((30, 30))
        self.image.fill("orange")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100, 200
        self.velocity_y = 0.5
        self.jump_force = 8
        self.is_jumping = False
        self.game_over = False

    def update(self, dt) -> None:
        self.velocity_y += GRAVITY
        self.rect.y += int(self.velocity_y)

        if self.is_jumping:
            self.velocity_y = -self.jump_force
            self.is_jumping = False

        if self.rect.y > TELA.get_height():
            self.game_over = True

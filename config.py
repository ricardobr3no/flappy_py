import pygame

pygame.font.init()

TELA = pygame.display.set_mode((360, 540))
GAME_OVER = False


# grupos
bird_group = pygame.sprite.GroupSingle()
pipes_group = pygame.sprite.Group()
pontuador_group = pygame.sprite.Group()
buttons_group = pygame.sprite.GroupSingle()

grupos = {
    "bird": bird_group,
    "pipes": pipes_group,
    "pontuador": pontuador_group,
    "buttons": buttons_group,
}
# fonts
font = pygame.font.SysFont("comic sans", 32)
font_G_over = pygame.font.SysFont("comic sans", 18)

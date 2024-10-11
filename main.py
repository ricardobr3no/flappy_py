import pygame
import sys

from config import grupos, TELA
from objects.bird import Bird
from objects.pipes import instanciar_pipes

pygame.init()
pygame.font.init()

# load
clock = pygame.time.Clock()
font = pygame.font.SysFont("comic sans", 32)
font_G_over = pygame.font.SysFont("comic sans", 18)
button_rect = pygame.Rect(110, 250, 150, 60)
running = True

bird = Bird()
grupos["bird"].add(bird)
spawn_rate = 0.9
best_score = score = 0
game_over = False


def spawn_pipes(dt):
    global spawn_rate
    spawn_rate -= dt
    if spawn_rate <= 0:
        instanciar_pipes()
        spawn_rate = 1


def pontuar():
    global score
    score_label = font.render(f"{score}", False, "white")
    score += 1
    TELA.blit(score_label, (TELA.get_width() // 2 - score_label.get_width() // 2, 20))


def restart():
    global score, game_over
    grupos["pipes"].empty()
    grupos["pontuador"].empty()

    score = 0
    game_over = False
    bird.load()


def show_game_over():
    global game_over, score, best_score
    game_over = True
    if score > best_score:
        best_score = score

    image = pygame.Surface((240, 360))
    image.fill("gray")
    #
    label_score = font.render(f"BEST: {best_score}", False, "purple")
    label_button = font.render("restart", False, "black")
    # draw
    image.blit(label_score, (50, 50))
    TELA.blit(image, (65, 120))
    pygame.draw.rect(TELA, "orange", button_rect)
    TELA.blit(label_button, (button_rect.left + 20, button_rect.top + 5))


while running:
    dt = clock.tick(60) / 1000
    spawn_pipes(dt)
    # loop de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            bird.is_jumping = True
        if event.type == pygame.MOUSEBUTTONUP and game_over:
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                restart()

    TELA.fill("blue")
    score_label = font.render(f"{score}", False, "white")
    TELA.blit(score_label, (TELA.get_width() // 2 - score_label.get_width() // 2, 20))
    # conditions
    colidiu = pygame.sprite.groupcollide(grupos["bird"], grupos["pipes"], False, False)
    pontuou = pygame.sprite.groupcollide(
        grupos["bird"], grupos["pontuador"], False, True
    )

    if colidiu or bird.game_over:
        show_game_over()

    elif not game_over:
        # conditions
        if pontuou:
            pontuar()
        # update and draw
        for grupo in grupos.values():
            grupo.update(dt)
            grupo.draw(TELA)

    pygame.display.flip()


pygame.quit()
sys.exit()

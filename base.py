import pygame
import sys

pygame.init()
tamanho  = ( 600, 400)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Game Título")
branco  = (255,255,255)
preto = (0, 0, 0)
posicaoXBolinha = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    tela.fill(branco)
    pygame.draw.circle(tela, preto, (posicaoXBolinha,200),50, 5)
    posicaoXBolinha = posicaoXBolinha + 1

    pygame.display.update()
    clock.tick(60)

    #pygame.draw.circle(tela, preto, (posicaoXBolinha,200),50, 5)
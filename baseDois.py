import pygame
import sys

pygame.init()
tamanho = (600, 400)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Game Título")
branco = (255, 255, 255)
preto = (0, 0, 0)

# Definir posições dos círculos
posicoes = [
    (150, 100),  # Círculo 1
    (450, 100),  # Círculo 2
    (150, 300),  # Círculo 3
    (450, 300)   # Círculo 4
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(branco)

    # Desenhar círculos
    for pos in posicoes:
        pygame.draw.circle(tela, preto, pos, 20)

    # Desenhar linhas conectando os círculos
    for i in range(len(posicoes)):
        for j in range(i + 1, len(posicoes)):
            pygame.draw.line(tela, preto, posicoes[i], posicoes[j], 2)

    pygame.display.update()
    clock.tick(60)
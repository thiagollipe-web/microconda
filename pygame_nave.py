import asyncio
import pygame

LARGURA, ALTURA = 640, 360
FPS = 60

async def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("MicroConda — Nave")
    relogio = pygame.time.Clock()

    jogador = pygame.Rect(LARGURA // 2 - 20, ALTURA - 55, 40, 25)
    velocidade = 5
    x = LARGURA // 2
    y = ALTURA // 2
    vx = 3
    vy = 2
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jogador.x -= velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jogador.x += velocidade
        jogador.x = max(0, min(LARGURA - jogador.width, jogador.x))

        x += vx
        y += vy
        if x <= 15 or x >= LARGURA - 15:
            vx *= -1
        if y <= 15 or y >= ALTURA - 90:
            vy *= -1

        tela.fill((5, 9, 18))
        pygame.draw.circle(tela, (98, 215, 255), (int(x), int(y)), 14)
        pygame.draw.polygon(
            tela,
            (110, 231, 162),
            [
                (jogador.centerx, jogador.top - 12),
                (jogador.left, jogador.bottom),
                (jogador.right, jogador.bottom),
            ],
        )
        pygame.display.flip()

        await asyncio.sleep(1 / FPS)

    pygame.quit()

await main()

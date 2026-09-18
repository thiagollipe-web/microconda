import asyncio
import pygame
import random

# MicroConda — Space Dodge
# Compatível com o modo Pygame do MicroConda Studio.

LARGURA = 640
ALTURA = 400
FPS = 60

async def main():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Space Dodge - MicroConda")

    FUNDO = (5, 8, 20)
    BRANCO = (240, 245, 255)
    AZUL = (70, 190, 255)
    VERMELHO = (255, 80, 90)
    AMARELO = (255, 220, 80)
    VERDE = (80, 230, 150)

    jogador = pygame.Rect(LARGURA // 2 - 20, ALTURA - 60, 40, 30)
    velocidade = 6

    meteoros = []
    for _ in range(5):
        meteoros.append({
            "x": random.randint(20, LARGURA - 20),
            "y": random.randint(-400, -20),
            "vel": random.randint(2, 5),
            "tamanho": random.randint(10, 20),
        })

    pontos = 0
    game_over = False
    rodando = True

    fonte = pygame.font.Font(None, 30)
    fonte_grande = pygame.font.Font(None, 58)

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif game_over and evento.key == pygame.K_r:
                    jogador.x = LARGURA // 2 - 20
                    pontos = 0
                    game_over = False
                    for meteoro in meteoros:
                        meteoro["x"] = random.randint(20, LARGURA - 20)
                        meteoro["y"] = random.randint(-400, -20)
                        meteoro["vel"] = random.randint(2, 5)

        if not game_over:
            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                jogador.x -= velocidade
            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                jogador.x += velocidade

            jogador.x = max(0, min(LARGURA - jogador.width, jogador.x))

            for meteoro in meteoros:
                meteoro["y"] += meteoro["vel"]

                if meteoro["y"] > ALTURA + 30:
                    meteoro["y"] = random.randint(-200, -20)
                    meteoro["x"] = random.randint(20, LARGURA - 20)
                    meteoro["vel"] = random.randint(2, 6)
                    pontos += 1

                area_meteoro = pygame.Rect(
                    int(meteoro["x"] - meteoro["tamanho"]),
                    int(meteoro["y"] - meteoro["tamanho"]),
                    meteoro["tamanho"] * 2,
                    meteoro["tamanho"] * 2,
                )

                if jogador.colliderect(area_meteoro):
                    game_over = True

        tela.fill(FUNDO)

        # Fundo estável: não altera o estado global do gerador a cada quadro.
        rng = random.Random(123)
        for _ in range(80):
            x = rng.randint(0, LARGURA - 1)
            y = rng.randint(0, ALTURA - 1)
            pygame.draw.circle(tela, BRANCO, (x, y), 1)

        for meteoro in meteoros:
            x = int(meteoro["x"])
            y = int(meteoro["y"])
            tamanho = meteoro["tamanho"]

            pygame.draw.circle(tela, VERMELHO, (x, y), tamanho)
            pygame.draw.circle(
                tela,
                AMARELO,
                (x - tamanho // 3, y - tamanho // 3),
                max(2, tamanho // 4),
            )

        if not game_over:
            pygame.draw.polygon(
                tela,
                AZUL,
                [
                    (jogador.centerx, jogador.top - 15),
                    (jogador.left, jogador.bottom),
                    (jogador.right, jogador.bottom),
                ],
            )
            pygame.draw.polygon(
                tela,
                VERDE,
                [
                    (jogador.centerx, jogador.top),
                    (jogador.centerx - 7, jogador.bottom - 5),
                    (jogador.centerx + 7, jogador.bottom - 5),
                ],
            )

        texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(texto, (15, 15))

        if game_over:
            titulo = fonte_grande.render("GAME OVER", True, VERMELHO)
            instrucao = fonte.render(
                "Pressione R para reiniciar",
                True,
                BRANCO,
            )

            tela.blit(
                titulo,
                (
                    LARGURA // 2 - titulo.get_width() // 2,
                    ALTURA // 2 - 50,
                ),
            )
            tela.blit(
                instrucao,
                (
                    LARGURA // 2 - instrucao.get_width() // 2,
                    ALTURA // 2 + 15,
                ),
            )

        pygame.display.flip()
        await asyncio.sleep(1 / FPS)

    pygame.quit()


await main()

# Space Invaders ASCII — teste do MicroConda Studio
# Controles: a = esquerda | d = direita | f = atirar | q = sair
# Cada comando avança uma rodada. O jogo funciona no navegador via prompt().

from js import prompt
from random import choice
from time import sleep

LARGURA = 31
ALTURA = 16
ALIEN_INICIAL = 9

player_x = LARGURA // 2
aliens = []
for y in (2, 4, 6):
    for x in range(3, LARGURA - 2, 4):
        aliens.append([x, y])

tiros = []
score = 0
turno = 0

def limpar():
    print("\n" * 4)

def desenhar():
    limpar()
    print("=" * LARGURA)
    print("        S P A C E  I N V A D E R S")
    print("=" * LARGURA)
    print(f"  SCORE: {score:04d}     ALIENS: {len(aliens):02d}")
    print("-" * LARGURA)

    quadro = [[" " for _ in range(LARGURA)] for _ in range(ALTURA)]

    for x, y in aliens:
        if 0 <= y < ALTURA:
            quadro[y][x] = "W"

    for x, y in tiros:
        if 0 <= y < ALTURA:
            quadro[y][x] = "|"

    quadro[ALTURA - 2][max(0, player_x - 1)] = "/"
    quadro[ALTURA - 2][player_x] = "A"
    quadro[ALTURA - 2][min(LARGURA - 1, player_x + 1)] = "\"

    for row in quadro:
        print("|" + "".join(row) + "|")

    print("=" * LARGURA)
    print(" A = ESQ   D = DIR   F = ATIRAR   Q = SAIR")

def mover_alienigenas():
    global aliens
    proximo = []
    for x, y in aliens:
        nx = x + (1 if turno % 4 < 2 else -1)
        ny = y + (1 if turno % 6 == 0 else 0)
        proximo.append([max(1, min(LARGURA - 2, nx)), ny])
    aliens = proximo

def atualizar_tiros():
    global tiros, score, aliens
    novos_tiros = []
    atingidos = set()

    for x, y in tiros:
        ny = y - 1
        alvo = None
        for i, (ax, ay) in enumerate(aliens):
            if ax == x and ay == ny:
                alvo = i
                break

        if alvo is not None:
            atingidos.add(alvo)
            score += 10
        elif ny >= 0:
            novos_tiros.append([x, ny])

    if atingidos:
        aliens = [a for i, a in enumerate(aliens) if i not in atingidos]

    tiros = novos_tiros

def jogar():
    global player_x, tiros, turno

    print("MICROCONDA • SPACE INVADERS ASCII")
    print("Uma versão simples para testar o Python no navegador.")
    print("Digite um comando e pressione Enter.")
    print()

    while True:
        desenhar()

        if not aliens:
            print("\n*** VITÓRIA! Você eliminou todos os invasores. ***")
            print(f"Pontuação final: {score}")
            break

        if any(y >= ALTURA - 2 for _, y in aliens):
            print("\n*** GAME OVER! Os invasores chegaram! ***")
            print(f"Pontuação final: {score}")
            break

        comando = prompt("Comando [A/D/F/Q]:")
        if comando is None:
            break

        comando = str(comando).strip().lower()[:1]

        if comando == "q":
            print("\nJogo encerrado. Até a próxima, piloto!")
            break
        elif comando == "a":
            player_x = max(1, player_x - 2)
        elif comando == "d":
            player_x = min(LARGURA - 2, player_x + 2)
        elif comando == "f":
            tiros.append([player_x, ALTURA - 3])
        else:
            print("Comando inválido.")

        atualizar_tiros()
        mover_alienigenas()
        turno += 1

jogar()

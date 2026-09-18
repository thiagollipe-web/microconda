# Space Invaders ASCII — modo navegador
# Execute este arquivo uma vez.
# Depois use no terminal: a = esquerda | d = direita | f = atirar | q = sair

LARGURA = 31
ALTURA = 14

estado = {
    "x": LARGURA // 2,
    "aliens": [],
    "tiros": [],
    "score": 0,
    "turno": 0,
    "ativo": True
}

def iniciar():
    estado["x"] = LARGURA // 2
    estado["aliens"] = []
    estado["tiros"] = []
    estado["score"] = 0
    estado["turno"] = 0
    estado["ativo"] = True
    for y in (1, 3, 5):
        for x in range(3, LARGURA - 2, 4):
            estado["aliens"].append([x, y])

def quadro():
    tela = [[" " for _ in range(LARGURA)] for _ in range(ALTURA)]
    for x, y in estado["aliens"]:
        if 0 <= x < LARGURA and 0 <= y < ALTURA:
            tela[y][x] = "W"
    for x, y in estado["tiros"]:
        if 0 <= x < LARGURA and 0 <= y < ALTURA:
            tela[y][x] = "|"
    x = estado["x"]
    tela[ALTURA - 2][max(0, x - 1)] = "/"
    tela[ALTURA - 2][x] = "A"
    tela[ALTURA - 2][min(LARGURA - 1, x + 1)] = "\"
    print("\n" + "=" * LARGURA)
    print("        SPACE INVADERS ASCII")
    print("=" * LARGURA)
    print(f"SCORE: {estado['score']:04d}   INVASORES: {len(estado['aliens']):02d}")
    print("-" * LARGURA)
    for linha in tela:
        print("|" + "".join(linha) + "|")
    print("=" * LARGURA)
    print("A esquerda | D direita | F atirar | Q sair")

def mover_tiros():
    novos = []
    removidos = set()
    for x, y in estado["tiros"]:
        ny = y - 1
        atingiu = None
        for i, (ax, ay) in enumerate(estado["aliens"]):
            if ax == x and ay == ny:
                atingiu = i
                break
        if atingiu is not None:
            removidos.add(atingiu)
            estado["score"] += 10
        elif ny >= 0:
            novos.append([x, ny])
    estado["tiros"] = novos
    if removidos:
        estado["aliens"] = [a for i, a in enumerate(estado["aliens"]) if i not in removidos]

def mover_invasores():
    passo = 1 if (estado["turno"] // 4) % 2 == 0 else -1
    for alien in estado["aliens"]:
        alien[0] += passo
        alien[0] = max(1, min(LARGURA - 2, alien[0]))
    if estado["turno"] % 8 == 0:
        for alien in estado["aliens"]:
            alien[1] += 1

def comando(tecla):
    tecla = str(tecla).lower()[:1]
    if tecla == "q":
        estado["ativo"] = False
        print("\nJOGO ENCERRADO.")
        return
    if not estado["ativo"]:
        print("O jogo terminou. Execute o arquivo novamente para reiniciar.")
        return
    if tecla == "a":
        estado["x"] = max(1, estado["x"] - 2)
    elif tecla == "d":
        estado["x"] = min(LARGURA - 2, estado["x"] + 2)
    elif tecla == "f":
        estado["tiros"].append([estado["x"], ALTURA - 3])
    else:
        print("Comando inválido. Use A, D, F ou Q.")
        return
    mover_tiros()
    mover_invasores()
    estado["turno"] += 1
    if any(y >= ALTURA - 2 for _, y in estado["aliens"]):
        estado["ativo"] = False
        quadro()
        print("\nGAME OVER — os invasores chegaram!")
        return
    if not estado["aliens"]:
        estado["ativo"] = False
        quadro()
        print(f"\nVITÓRIA! Pontuação: {estado['score']}")
        return
    quadro()

iniciar()
print("MicroConda: Space Invaders carregado.")
quadro()

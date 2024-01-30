import random

PS_jugador = (100, 100)
PS_oponente = (100, 100)

ataques_jugador = ((10, 0), (35, 0), (20, 0))
ataques_oponente = ((10, 10), (35, 0), (40, 0))

while PS_jugador[0] > 0 and PS_oponente[0] > 0:
    ataque_jugador = input("Entre malicioso, ascuas y placaje, decide y haz tu ataque: ")
    if ataque_jugador.lower() == "malicioso":
        PS_oponente = (PS_oponente[0] - ataques_jugador[0][0], PS_oponente[1])
        if PS_oponente[0] <= 0:
            PS_oponente = (1, PS_oponente[1])
    elif ataque_jugador == "placaje":
        defensa_oponente = PS_oponente[1]
        PS_oponente = (PS_oponente[0] - (35 / (defensa_oponente / 100)), PS_oponente[1] - 10)
        if PS_oponente[0] <= 0:
            PS_oponente = (1, PS_oponente[1])
    elif ataque_jugador == "ascuas":
        PS_oponente = (PS_oponente[0] - ataques_jugador[2][0], PS_oponente[1])
    else:
        print("¡¿Qué estás haciendo?! ¡Tus ataques son malicioso, placaje y ascuas!")

    # El jugador ha atacado, turno del oponente
    ataque_oponente = random.choice(ataques_oponente)
    if ataque_oponente == ataques_oponente[0]:
        PS_jugador = (PS_jugador[0] - ataque_oponente[0], PS_jugador[1] - ataque_oponente[1])
        if PS_jugador[0] <= 0:
            PS_jugador = (1, PS_jugador[1])
        if PS_jugador[1] <= 0:
            PS_jugador = (PS_jugador[0], 1)
    elif ataque_oponente == ataques_oponente[1]:
        defensa_jugador = PS_jugador[1]
        PS_jugador = (PS_jugador[0] - (35 * (100 / defensa_jugador)), PS_jugador[1])
        if PS_jugador[0] <= 0:
            PS_jugador = (1, PS_jugador[1])
    elif ataque_oponente == ataques_oponente[2]:
        PS_jugador = (PS_jugador[0] - ataque_oponente[0], PS_jugador[1])
        if PS_jugador[0] <= 0:
            PS_jugador = (1, PS_jugador[1])

# La batalla ha finalizado
if PS_oponente[0] <= 0:
    print("¡Felicidades, has ganado!")
elif PS_oponente[0] <= 0 and PS_jugador[0] <= 0:
    print("¡Empate!")
else:
    print("Lo siento, has perdido.")

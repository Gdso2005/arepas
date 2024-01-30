import random #ataque con randrange

PS_jugador = 100 
Ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

ataque_jugador = ["malicioso", "placaje", "ascuas"]
ataque_oponente = ["latigo", "placaje", "pistola de agua"]

while PS_jugador > 0 and Ps_oponente > 0:
    ataque_jugador = input("Entre malicioso, ascuas y placaje, decide y Haz tu ataque: ")
    if ataque_jugador.lower() not in ataque_jugador:
        print("Que estas haciendo?! Tus ataques son maliciosos, placaje, y ascuas!")
        continue

    ataque_oponente = random.choice(ataque_oponente)

    if ataque_jugador.lower() == "malicioso":
        defensa_oponente = max(1, defensa_oponente - 10)
    elif ataque_jugador == "placaje":
        Ps_oponente -= 35 / (defensa_oponente / 100)
    elif ataque_jugador == "ascuas":
        Ps_oponente -= 20

    if ataque_oponente == "latigo":
        defensa_jugador = max(1, defensa_jugador - 10)
    elif ataque_oponente == "placaje":
        PS_jugador -= 35 * (100 / defensa_jugador)        
    elif ataque_oponente == "pistola de agua":
        PS_jugador -= 40

#la batalla ha finalizado
if Ps_oponente <= 0 :
    print("Felicidades, has ganado")
elif Ps_oponente <= 0 and PS_jugador <= 0:
    print("empate")
else: #ya sabemos que el oponente es > 0
    print("Lo siento, has perdido")

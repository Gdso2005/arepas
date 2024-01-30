import random #hora de decidir el ataque con Randrange


PS_jugador = 100 
Ps_oponente = 100
defensa_oponente=100
defensa_jugador=100

ataque_jugador: ["malicioso","placaje","ascuas"]
ataque_oponente: ["latigo","placaje","pistola de agua"]
while PS_jugador > 0 and Ps_oponente> 0:
    ataque_jugador= input ("Entre malicioso, ascuas y placaje, decide y Haz tu ataque: ")
    if ataque_jugador.lower() == "malicioso":
        defensa_oponente = defensa_oponente - 10
        if defensa_oponente <= 0:
            defensa_oponente = 1
    elif ataque_jugador == "placaje":
        Ps_oponente -= 35 /(defensa_oponente/100)
    elif ataque_jugador == "ascuas":
        Ps_oponente -= 20
    else:
        print("Que estas haciendo?! Tus ataques son maliciosos, placaje, y ascuas!")


#el jugador ha atacado, turno del oponente
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente == 1: #latigo
        defensa_jugador -= 10
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque_oponente == 2 : #placaje
        PS_jugador -= 35 * (100/defensa_jugador)        
    elif ataque_oponente == 3: #Pistola de agua
        PS_jugador -= 40
    #randrange esta garantizado a ser 1,2 o 3
        
        
#la batalla ha finalizado
if Ps_oponente <= 0 :
    print("Felicidades, has ganado")
elif Ps_oponente <= 0 and PS_jugador <= 0:
    print("empate")
else: #ya sabemos que el oponente es > 0
    print("Lo siento, has perdido")
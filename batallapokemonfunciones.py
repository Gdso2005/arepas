import random

def ataque_jugador(salud_actual, defensa_actual, ataque_elegido):
    """
    Calcula los nuevos valores de salud y defensa después del ataque del jugador.
    
    Args:
        salud_actual (float): Puntos de salud actuales del jugador siendo atacado.
        defensa_actual (float): Puntos de defensa actuales del jugador siendo atacado.
        ataque_elegido (str): Ataque seleccionado por el jugador ("malicioso", "placaje" o "ascuas").
    
    Returns:
        tuple: Nuevos valores de salud y defensa en una tupla.
    """
    if ataque_elegido.lower() == "malicioso":
        defensa_actual -= 10
        if defensa_actual <= 0:
            defensa_actual = 1
    elif ataque_elegido.lower() == "placaje":
        salud_actual -= 35 / (defensa_actual / 100)
    elif ataque_elegido.lower() == "ascuas":
        salud_actual -= 20
    else:
        print("¡Ataque no válido!")

    return salud_actual, defensa_actual

def ataque_oponente(salud_actual, defensa_actual):
    """
    Calcula los nuevos valores de salud y defensa después del ataque del oponente.
    
    Args:
        salud_actual (float): Puntos de salud actuales del jugador siendo atacado.
        defensa_actual (float): Puntos de defensa actuales del jugador siendo atacado.
    
    Returns:
        tuple: Nuevos valores de salud y defensa en una tupla.
    """
    ataque_elegido = random.choice(["latigo", "placaje", "pistola de agua"])
    if ataque_elegido == "latigo":
        defensa_actual -= 10
        if defensa_actual <= 0:
            defensa_actual = 1
    elif ataque_elegido == "placaje":
        salud_actual -= 35 * (100 / defensa_actual)
    elif ataque_elegido == "pistola de agua":
        salud_actual -= 40

    return salud_actual, defensa_actual

# Ejemplo de uso
PS_jugador = 100
defensa_jugador = 100

while PS_jugador > 0:
    ataque_jugador_elegido = input("Elige tu ataque (malicioso, placaje o ascuas): ")
    PS_jugador, defensa_jugador = ataque_jugador(PS_jugador, defensa_jugador, ataque_jugador_elegido)
    PS_jugador, defensa_jugador = ataque_oponente(PS_jugador, defensa_jugador)

if PS_jugador <= 0:
    print("Lo siento, has perdido.")
else:
    print("¡Felicidades, has ganado!")

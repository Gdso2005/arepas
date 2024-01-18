def es_bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False

anio = int(input("Ingrese un año entre 1900 y 2199: "))
bisiestos = 0
for i in range(1900, anio + 1):
    if es_bisiesto(i):
        bisiestos += 1

print("El número de años bisiestos entre 1900 y", anio, "es", bisiestos)

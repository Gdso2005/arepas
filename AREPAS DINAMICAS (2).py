def preparar_arepas():
    print("¡Preparación de Arepas!")
    
    # Solicitar ingredientes al usuario
    taza_agua = input("Ingresa la cantidad de taza de agua: ")
    taza_harina_pan = input("Ingresa la cantidad de taza de harina PAN: ")
    cdta_sal = input("Ingresa la cantidad de cucharadita de sal: ")
    cda_aceite = input("Ingresa la cantidad de cucharada de aceite: ")

    # Conversión de strings a números
    try:
        taza_agua = float(taza_agua)
        taza_harina_pan = float(taza_harina_pan)
        cdta_sal = float(cdta_sal)
        cda_aceite = float(cda_aceite)
    except ValueError:
        print("Error: Debes ingresar valores numéricos para los ingredientes.")
        return

    # Mostrar los ingredientes ingresados
    print("\nIngredientes ingresados:")
    print(f"Taza de Agua: {taza_agua} unidades")
    print(f"Taza de Harina PAN: {taza_harina_pan} unidades")
    print(f"Cucharadita de Sal: {cdta_sal} unidades")
    print(f"Cucharada de Aceite: {cda_aceite} unidades")

    # Pasos para preparar las arepas
    print("\nPasos para preparar las arepas:")
    print("1. En un bol, vierte el agua, la harina y la sal.")
    print("2. Mezcla hasta que quede uniforme.")
    print("3. Dale a la mezcla forma de disco.")
    print("4. Coloca la mezcla con el aceite en un budare hasta que se dore.")
    print("5. Voltea la arepa y repite el paso anterior.")
    print("6. Sirve la arepa en un plato.")

# Llamar a la función principal
preparar_arepas()

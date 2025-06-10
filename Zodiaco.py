
# Lista de signos del zodiaco con sus fechas
signos = [
    ("Capricornio", (22, 12), (19, 1)),
    ("Acuario", (20, 1), (18, 2)),
    ("Piscis", (19, 2), (20, 3)),
    ("Aries", (21, 3), (19, 4)),
    ("Tauro", (20, 4), (20, 5)),
    ("Géminis", (21, 5), (20, 6)),
    ("Cáncer", (21, 6), (22, 7)),
    ("Leo", (23, 7), (22, 8)),
    ("Virgo", (23, 8), (22, 9)),
    ("Libra", (23, 9), (22, 10)),
    ("Escorpio", (23, 10), (21, 11)),
    ("Sagitario", (22, 11), (21, 12)),
    ("Capricornio", (22, 12), (31, 12))
]

# Alias de signos sin acentos y en minúsculas para que el usuario pueda escribir sin errores
alias_signos = {
    "aries": "Aries",
    "tauro": "Tauro",
    "geminis": "Géminis",
    "géminis": "Géminis",
    "cancer": "Cáncer",
    "cáncer": "Cáncer",
    "leo": "Leo",
    "virgo": "Virgo",
    "libra": "Libra",
    "escorpio": "Escorpio",
    "sagitario": "Sagitario",
    "capricornio": "Capricornio",
    "acuario": "Acuario",
    "piscis": "Piscis"
}

# Lista de elementos con su signo
elementos = {
    "Aries": "Fuego",
    "Tauro": "Tierra",
    "Géminis": "Aire",
    "Cáncer": "Agua",
    "Leo": "Fuego",
    "Virgo": "Tierra",
    "Libra": "Aire",
    "Escorpio": "Agua",
    "Sagitario": "Fuego",
    "Capricornio": "Tierra",
    "Acuario": "Aire",
    "Piscis": "Agua"
}

# Lista de descripciones
descripciones = {
    "Aries": "Impulsivo, valiente, lleno de energía y con iniciativa.",
    "Tauro": "Paciente, leal, estable y amante del confort.",
    "Géminis": "Comunicativo, curioso, adaptable y con mente rápida.",
    "Cáncer": "Emocional, protector, sensible y muy familiar.",
    "Leo": "Líder, creativo, generoso y con gran confianza.",
    "Virgo": "Analítico, perfeccionista, lógico y muy trabajador.",
    "Libra": "Diplomático, equilibrado, sociable y amante de la armonía.",
    "Escorpio": "Apasionado, intenso, misterioso y determinado.",
    "Sagitario": "Optimista, aventurero, sincero y amante de la libertad.",
    "Capricornio": "Responsable, disciplinado, ambicioso y constante.",
    "Acuario": "Innovador, independiente, original y humanitario.",
    "Piscis": "Empático, soñador, intuitivo y muy sensible."
}

# colores
colores_elementos = {
    "Fuego": "\033[91m",   # Rojo
    "Tierra": "\033[92m",  # Verde
    "Aire": "\033[96m",    # Azul claro
    "Agua": "\033[94m"     # Azul
}

# Color ANSI
def color_barra(porcentaje):
    if porcentaje >= 75:
        color = "\033[92m"  # Verde
    elif porcentaje >= 60:
        color = "\033[93m"  # Amarillo
    else:
        color = "\033[91m"  # Rojo
    return color

def mostrar_menu():
    print("\n=== Menú del Zodiaco ===")
    print("1. Saber tu signo del zodiaco")
    print("2. Compatibilidad entre signos")
    print("3. Salir")




# Funcion de obtener el signo
def obtener_signo_zodiaco(dia, mes):
    for signo, (dia_inicio, mes_inicio), (dia_fin, mes_fin) in signos:
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            return signo
    return "Fecha Invalida"

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("\n=== Saber tu signo del zodiaco ===")
        fecha_input = input("Escribe tu fecha de nacimiento (dia/mes): ")
        dia_str, mes_str = fecha_input.split("/")
        dia = int(dia_str)
        mes = int(mes_str)

        signo = obtener_signo_zodiaco(dia, mes)
        elemento = elementos.get(signo, "Elemento no encontrado")
        descripcion = descripciones.get(signo, "Descripcion no encontrada")

# Colores
        color = colores_elementos.get(elemento, "\033[0m")  # Color por defecto si no se encuentra
        reset_color = "\033[0m"  
        


        print(f"{color}Tu signo del zodiaco es : {signo}")
        print(f"Tu Elemento es : {elemento}")
        print(f"Descripcion: {descripcion}{reset_color}")

    elif opcion == "2":
        print("=== Compatibilidad entre signos ===")
        signo1 = input("Introduce el primer signo: ").lower()
        signo2 = input("Introduce el segundo signo: ").lower()

        signo1 = alias_signos.get(signo1)
        signo2 = alias_signos.get(signo2)

        if signo1 not in elementos or signo2 not in elementos:
            print("Uno de los signos no es válido.")
        else:
            elem1 = elementos[signo1]
            elem2 = elementos[signo2]

            # Compatibilidades entre signos

            compatibles = {
                "Fuego": ["Fuego", "Aire"],
                "Tierra": ["Tierra", "Agua"],
                "Aire": ["Aire", "Fuego"],
                "Agua": ["Agua", "Tierra"]
            }
            if elem2 in compatibles[elem1]:
                porcentaje = 90 if elem1 == elem2 else 75
            elif elem1 == elem2:
                porcentaje = 60
            else:
                porcentaje = 40

            # Barra visual
            barra = "█" * (porcentaje // 10) + "-" * (10 - (porcentaje // 10))
            barra_color = color_barra(porcentaje)
            reset = "\033[0m"  # Para volver al color por defecto"

            print(f"\nCompatibilidad entre {signo1} ({elem1}) y {signo2} ({elem2}):")
            print(f"[{barra_color}]{barra} {porcentaje}%{reset}")

    elif opcion == "3":
        print("Adios adicto al zodiaco!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")




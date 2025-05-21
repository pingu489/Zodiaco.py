
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





# Funcion de obtener el signo
def obtener_signo_zodiaco(dia, mes):
    for signo, (dia_inicio, mes_inicio), (dia_fin, mes_fin) in signos:
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            return signo
    return "Fecha Invalida"


# Pedir la fecha y mostrar el resultado
fecha_input= input("Escribe tu fecha de nacimiento (dia/mes): ")
dia_str, mes_str = fecha_input.split("/")
dia = int(dia_str)
mes = int(mes_str)

signo = obtener_signo_zodiaco(dia, mes)
elemento = elementos.get(signo, "Elemento no encontrado")
descripcion = descripciones.get(signo, "Descripcion no encontrada")


# Colores
color = colores_elementos.get(elemento, "\033[0m")  # Color por defecto si no se encuentra
reset_color = "\033[0m"   # Para volver al color por defecto



print(f"{color}Tu signo del zodiaco es : {signo}")
print(f"Tu Elemento es : {elemento}")
print(f"Descripcion: ´{descripcion}")

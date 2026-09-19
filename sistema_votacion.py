# Candidatos disponibles para votar
CANDIDATOS = ["Candidato A", "Candidato B", "Candidato C"]

# Conteo de votos: {candidato: cantidad}
votos = {candidato: 0 for candidato in CANDIDATOS}

# Control de personas que ya votaron: {id_persona: candidato_votado}
votantes = {}


def registrar_voto(id_persona, candidato):
    """
    Registra el voto de una persona.
    Debe validar que la persona no haya votado antes
    y que el candidato exista. (Implementar en rama-registro)
    """
    raise NotImplementedError("Pendiente: implementar en rama-registro")


def ver_resultados():
    """
    Muestra el conteo de votos y el porcentaje que representa
    cada candidato sobre el total de votos emitidos.
    (Implementar en rama-resultados)
    """
    raise NotImplementedError("Pendiente: implementar en rama-resultados")


def reiniciar_votacion():
    """
    Guarda el resultado actual en un archivo de historial
    y reinicia los conteos y la lista de votantes.
    (Implementar en rama-reinicio)
    """
    raise NotImplementedError("Pendiente: implementar en rama-reinicio")


def menu():
    opciones = {
        "1": lambda: registrar_voto(input("ID persona: "), input("Candidato: ")),
        "2": ver_resultados,
        "3": reiniciar_votacion,
    }
    while True:
        print("\n--- SISTEMA DE VOTACIÓN ---")
        print("1. Registrar voto")
        print("2. Ver resultados")
        print("3. Reiniciar votación")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "4":
            break
        accion = opciones.get(opcion)
        if accion:
            try:
                accion()
            except NotImplementedError as e:
                print(e)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()

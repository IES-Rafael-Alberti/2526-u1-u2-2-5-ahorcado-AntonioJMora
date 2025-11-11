"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Antonio Jesús Mora Cabeza
Fecha: 11/11/2025
"""


def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola y ocultar la palabra para el jugador 2.
    """
    print("\n" * 50)


def solicitar_palabra():
    """
    Solicita una palabra al jugador 1

    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns
    -------
    str
        La palabra a adivinar en mayúsculas
    """

    palabra = input("Jugador 1: Introduce la palabra a adivinar (mínimo 5 letras): ").upper()
    while len(palabra) < 5 or not palabra.isalpha():
        palabra = input("Jugador 1: Introduce la palabra a adivinar (mínimo 5 letras): ").upper()
    return palabra


def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2 y valida que no este ya usada
    
    Parameters
    ----------
    letras_usadas: list
        Lista de letras ya introducidas

    Returns
    -------
    str
        La letra introducida en mayúsculas
    """

    letra = input("Introduce una letra: ").upper()
    while len(letra) != 1 or not letra.isalpha() or letra in letras_usadas:
        letra = input("Introduce una letra: ").upper()
    letras_usadas.append(letra)
    return letra


def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego
    
    Parameters
    ----------
    palabra_oculta: str
        La palabra con _ y letras adivinadas
    intentos: int
        Número de intentos restantes
    letras_usadas: list
        Lista de letras ya usadas
    """

    print(f"Intentos restantes: {intentos}")
    print("Palabra: " + " ".join(palabra_oculta))
    print(f"Letras usadas: {letras_usadas}")

def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Parameters
    ----------
    palabra: str
        La palabra completa a adivinar
    palabra_oculta: str
        La palabra actual con _ y letras adivinadas
    letra: str
        La letra que se ha adivinado
        
    Returns
    -------
    str
        La palabra oculta actualizada
    """

    lista_palabra_oculta = list(palabra_oculta)

    for indice, caracter in enumerate(palabra):
        if caracter == letra:
            lista_palabra_oculta[indice] = letra

    return "".join(lista_palabra_oculta)


def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")

    # Configuración inicial
    INTENTOS_MAXIMOS = 5

    # Solicitar la palabra al jugador 1
    palabra = solicitar_palabra()

    # Limpiar la pantalla para que el jugador 2 no vea la palabra
    limpiar_pantalla()

    #Inicializar variables del juego
    # - palabra_oculta: string con guiones bajos (ej: "_ _ _ _ _")
    # - intentos: número de intentos restantes
    # - letras_usadas: lista vacía
    # - juego_terminado: False
    palabra_oculta = "_"*len(palabra)
    intentos = INTENTOS_MAXIMOS
    letras_usadas = []
    juego_terminado = False

    print("Jugador 2: ¡Adivina la palabra!\n")

    # Bucle principal del juego
    while intentos > 0 and not juego_terminado:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        letra = solicitar_letra(letras_usadas)

        if letra in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print(f"¡Bien! La letra {letra} está en la palabra.")
            print("\n")
        else:
            intentos -= 1
            print("¡Letra incorrecta!")
            print("\n")
        if "_" not in palabra_oculta:
            juego_terminado = True

    # TODO: Mostrar mensaje final

    if juego_terminado == True:
        print(f"¡FELICIDADES! Has adivinado la palabra: {palabra}")
    else:
        print("¡GAME OVER! Te has quedado sin intentos.")
        print(f"La palabra era: {palabra}")


def main():
    """
    Punto de entrada del programa
    Inicia el juego y pregunta si se desea jugar de nuevo.
    """
    jugar()

    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")

    if jugar_otra_vez.lower() == "s":
        main()

if __name__ == "__main__":
    main()

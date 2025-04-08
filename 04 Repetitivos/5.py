# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (Entre 0 y 9): "))
    intentos += 1
    if intento == secreto:
        print("Respuesta correcta. Lo adivinaste en ", intentos, " intento/s.")
        break

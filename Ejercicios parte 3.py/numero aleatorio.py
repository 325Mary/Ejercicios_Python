'''Utilizando la función randrange del módulo random, escribir un programa que obtenga
un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
sin son menores o mayores que el número a adivinar, hasta que el usuario ingrese el
número correcto.'''


import random

def adivinar_numero():
    numero_secreto = random.randrange(1, 101)  # Genera un número secreto entre 1 y 100
    intentos = 0

    while True:
        intentos += 1
        numero_ingresado = int(input("Ingresa un número: "))

        if numero_ingresado < numero_secreto:
            print("El número ingresado es menor al número secreto.")
        elif numero_ingresado > numero_secreto:
            print("El número ingresado es mayor al número secreto.")
        else:
            print(f"¡Felicitaciones! Adivinaste el número secreto en {intentos} intentos.")
            break

adivinar_numero()









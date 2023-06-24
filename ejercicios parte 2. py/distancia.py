'''Construye un programa que Si distancia es mayor que 20 y menos que 35, leer un
valor para tiempo y calcular  la  Velocidad si   Distancia = Velocidad * Tiempo'''

distancia = float(input("Ingrese la distancia: "))


if distancia > 20 and distancia < 35:
    tiempo = float(input("Ingrese el tiempo: "))
    velocidad = distancia / tiempo
    print("La velocidad es: ", velocidad)
else:
    velocidad= float(input("Ingrese la velocidad: "))
    tiempo = float(input("Ingrese el tiempo: "))
    distancia = velocidad * tiempo
    print("La distancia es : ", distancia)
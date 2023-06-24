'''Utiliza una Estructura selectiva para averiguar si un año leído de teclado es o no
bisiesto'''

diasAÑO = int(input("Ingrese el numero de dias por año: "))

if diasAÑO == 365:
    print("Año no biciesto.")
elif diasAÑO == 366:
    print("Año biciesto")
else:
    print("Numero de dias incorrecto!!")
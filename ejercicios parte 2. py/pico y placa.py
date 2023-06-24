'''Realizar  un programa para saber que día tiene pico y placa su vehículo'''
placa =input("Ingrese la placa de su vehiculo: ")

if len(placa) == 5 :
    try:
        x = int(placa[5])
    except:
        x = int(placa[4])
    if x == 1 or x == 2:
        print("Tiene pico y placa Lunes.")
    elif x == 3 or x == 4:
        print("Tiene pico y placa Martes.")
    elif x == 5 or x == 6:
        print("Tiene pico y placa Miercoles.")
    elif x == 7 or x == 8:
        print("Tiene pico y placa Jueves.")
    elif x == 9 or x == 0:
        print("Tiene pico y placa Viernes.")
else: 
    print("Error!!!! de escritura Ejemplo:")
    print("Carro: ghc562")
    print("Moto: ghc55t")

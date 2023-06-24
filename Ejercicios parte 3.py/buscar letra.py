'''El usuario ingresa por teclado una oración por ejemplo 'Las cuentas claras y el
chocolate espeso' el programa debe permitir buscar la  letra que el usuario quiere
buscar y contar cuantas letras hay; Ejemplo: letra a buscar 's'; 'Las cuentas claras y
el chocolate espeso' posee 4 letras 's'''

def contar_letra(oracion, letra):
    contador = 0
    for caracter in oracion:
        if caracter == letra:
            contador += 1
    return contador

oracion = input("Ingrese una oracion: ")
letra = input("Ingrese la letra que desea buscar: ")

total_letras = contar_letra (oracion, letra)
print("La oracion: ", oracion, "tiene ", total_letras, "letras ")
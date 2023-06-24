'''Escribir una función 'es_potencia_de_dos' que reciba como parámetro un número
natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
también incluir una función que, dados dos números naturales pasados como
parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango
formado por esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar
la función es_potencia_de_dos, descrita en el punto anterior.Números perfectos y
números amigo'''


def es_potencia_de_dos(numero):
    while numero > 1:
        if numero % 2 != 0:
            return False
        numero = numero // 2
    return True


def suma_potencias_de_dos(num1, num2):
    suma = 0
    for i in range(num1, num2+1):
        if es_potencia_de_dos(i):
            suma += i
    return suma
numero = int(input("Ingrese el numero: "))
num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))


print(es_potencia_de_dos(numero))  
 
print(suma_potencias_de_dos(num1,num2))  

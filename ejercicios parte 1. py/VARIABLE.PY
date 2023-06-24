'''Cree las variables y asigne los siguientes valores y Muestre la información
en consola de los datos ingresados
nombre = “Andres”
edad = 18
identificacion = “1061555333”
mayor_de_edad = edad >= 18'''

nombre = input("Ingrese el nombre: ")

edad = int(input("Ingresar la edad: "))

identificacion = input("Ingresar identificacion: ")

while edad > 0:
    if edad >= 18:
        print("Mayor de edad")
    else: 
        print("Es menor de edad.")
    break
print("su nombres es: ", nombre)
print("Su edad es: ", edad, "años")
print("Su identificacion es: ", identificacion)

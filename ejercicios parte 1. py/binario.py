'''Elaborar un programa  que  convierta  un  numero decimal ingresado  por teclado a
numero  binario, al final  deberá mostrar cual es su equivalencia'''

'''numero = int(input("ingrese el numero: "))
binario = []
while numero != 0:

    cociente = numero / 2
    modulo = numero % 2
    numero = cociente
    binario.append(modulo)

rev = list(reversed(binario))
print(rev)'''

numero = int(input("Ingrese el número: "))
binario = []

while numero != 0:
    cociente = numero // 2
    modulo = numero % 2
    numero = cociente
    binario.append(modulo)


    numero = cociente
   
# Invertir la lista
binario.reverse()

print("Representación binaria:", binario)
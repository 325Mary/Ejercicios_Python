'''Se desea realizar una estadística de los pesos de los alumnos de un colegio de
acuerdo a la siguiente tabla:
Alumnos de menos de 40 kg.
Alumnos entre 40 y 50 kg.
Alumnos de más de 50 kg y menos de 60 kg.
Alumnos de más o igual a 60 kg.'''

n = int(input("Introducir numero de alumnos: "))
a = 0
b = 0
c = 0
d = 0


for i in range (n):
    peso = int(input("Ingresar peso: "))
    if peso < 40 :
        a = a + 1
    elif peso >= 40 and peso <= 50:
        b = b + 1
    elif peso > 50  and peso <60:
        c = c + 1
    elif peso  >= 60 :
        d = d + 1
    else:
        print("peso incorrecto!!!!")

total1= (a / n)*100
total2= (b / n)*100
total3= (c / n)*100
total4= (d / n)*100
print(total1, "%", "menos de 40")
print(total2, "%","entre 40 y 50" )
print(total3, "%","mas de 50 y menos de 60") 
print(total4, "%", "mayor de 60")

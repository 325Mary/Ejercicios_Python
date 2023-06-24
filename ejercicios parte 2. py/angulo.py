'''Un ángulo se considera agudo si es menor de 90 grados, obtuso si es mayor de 90
grados y recto si es igual a 90 grados. Utilizando esta información, escribir un
algoritmo que acepte un ángulo en grados y visualice el tipo de ángulo
correspondiente a los grados introducidos'''

n1= int(input("Introduce el primer angulo: "))
n2 = int(input("Introduce el segumdo angulo: "))
n3 = (n1 + n2) - 180

if n3 < 90:
    print("El angulo es agudo: ", n3)
elif n3 > 90:
    print("El angulo es obtuso", n3)
elif n3 == 90:
    print("El angulo es recto", n3)
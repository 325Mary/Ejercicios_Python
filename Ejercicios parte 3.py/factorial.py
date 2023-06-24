'''Calcular el factorial de un numero ingresado  por teclado, si el  factorial de un numero
se  representa de la siguiente forma n! = 1*2*3*4*5......(n-1)*n    Ejemplo 2: 4! =
1*2*3*4  = 24; tenga en cuenta que el  factorial de 0! es 1   0! = 1'''


n = int(input("Ingrese el factorial: "))
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado

fact=factorial(n)
print(fact)

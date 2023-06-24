'''Empleo de estructura selectiva para detectar si un número es entero o real'''
n1 = 2.0

if type(n1) == int:
    print("Es entero.")
elif type(n1) == float:
    print("Es real.")
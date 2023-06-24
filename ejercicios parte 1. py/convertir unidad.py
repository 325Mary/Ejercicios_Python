'''De acuerdo con la tabla realice un programa que convierta una unidad a otra unidad,
por  ejemplo  si el usuario ingresa 1 MB el  sistema  deberá  arrojar  el siguiente
resultado 
1MB son:
8388608 Bits
1048576 Bytes
1024 Kb
0.000976563 GB'''
MB = int(input("Ingrese los numeros de megaBites: "))
bits = 83886008 * MB
bytes= 1048576 * MB
kb = 1024 * MB
GB = 0.000976563 * MB

print(MB, "MG  son: ")
print(bits, "bits")
print(bytes, "bytes")
print(kb, "Kb")
print(GB, "GB")
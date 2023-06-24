'''Calcule el  valor  del  IVA 19% y el descuento de un producto ingresado
por teclado'''
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))
valor = int(input("Ingrese el valor: "))
sub_total = cantidad * valor
iva = int(sub_total * 0.19)
total =int( sub_total + iva)

print("Producto: ", producto)
print("cantidad: ", cantidad)
print("valor: ", valor )
print("SubTotal: ", sub_total)
print("Iva 19%: ", iva)
print("Total: ", total)
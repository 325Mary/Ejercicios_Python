'''Calcule el  valor  del  IVA 19% y el descuento de un producto ingresado por teclado'''

Producto = input("ingrese el producto: ")
cantidad = int(input("ingrese la cantidad :"))
valor = int(input("ingrese el valor: "))
total = cantidad * valor 
iva = total * 0.19
descuento = 0.10
print("total: ", total)
print("iva: ", iva)
if  Producto == Producto :
    print("Descuento es de: " + str(descuento * total))   
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y
# calcule e imprima por pantalla el precio final del artículo.

price = float(input("Introduzca el importe sin IVA: "))
IVA = float(input("Introduzca el IVA a aplicar: "))

final_price = price + ((price * IVA) / 100)

print ("El precio final del producto es de " + str(final_price))
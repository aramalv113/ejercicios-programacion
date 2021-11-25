# Escribe un programa que pida el importe final de un artículo y calcule e imprima por
# pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un
# tipo de IVA del 10%).

price_with_IVA = float(input("Introduzca el precio del producto: "))
IVA = 21 # 10% sobre el precio final

price_without_IVA = price_with_IVA - ((price_with_IVA * IVA) / 100.0)

print ("El precio del producto sin IVA(" + str(IVA) + "%) es de " + str(price_without_IVA))

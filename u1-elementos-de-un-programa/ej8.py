# Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma,
# pero solo usando dos variables diferentes.

numero = float(input("Introduzca primer número: "))

suma = numero;

numero = float(input("Introduzca segundo número: "))

suma = suma + numero;

numero = float(input("Introduzca tercer número: "))

suma = suma + numero;

print ("n1 + n2 + n3 = " + str(suma))
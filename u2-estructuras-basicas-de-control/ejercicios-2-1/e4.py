# Escribe un programa que solicite un número al usuario e indique si es par o impar.

try:
    numero = int(input("Introduce un número: "))
    
    if numero%2==0:
        print("El número",numero,"es par")
    else:
        print("El número",numero,"es impar")
        
except ValueError:
    print("No has introducido un dato numérico")
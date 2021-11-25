import os

os.system("cls")

if __name__=="__main__":
    cadena = input("Cadena: ")

    print("a) imprime los dos primeros caracteres --> ", end="")
    print("Forma 1: " + cadena[0:2] + " / Forma 2: " + cadena[:2])

    print("b) imprime los tres últimos caracteres --> ", end="")
    print("Forma 1: " + cadena[-3:len(cadena)] + " / Forma 2: " + cadena[-3:])

    print("c) imprime la cadena cada dos caracteres --> ", end="")
    print("Forma 1: " + cadena[0:len(cadena):2] + " / Forma 2: " + cadena[::2])

    print("d) imprime la cadena en orden inverso --> ", end="")
    print("Forma 1: " + cadena[-1:(-1*len(cadena)-1):-1] + " / Forma 2: " + cadena[::-1])

    print("e) imprime la cadena en un sentido y en sentido inverso --> ", end="")
    print(cadena[:len(cadena)] + cadena[::-1])
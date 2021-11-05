import os

os.system("cls")

while True:
    hexadecimal = input("Número en formato hexadecimal: ").lower()
    decimal = 0
    incorrectos = ""

    for h in hexadecimal:
        if h not in ('1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'):
            incorrectos += h + ' '
    
    if len(incorrectos) > 0:
        print(f" >> Los caracteres '{incorrectos.rstrip(incorrectos[-1])}' del número '{hexadecimal}' no se reconocen con el formato hexadecimal.")
        continue

    # Los números, sin importar en qué base estén, empiezan con exponente 0 para las unidades en adelante, por lo que si la cadena vale 5, tendremos
    # que restar 1 para decir que iremos del exponente 0 al exponente 4 (en total, 5)
    exponente = len(hexadecimal) - 1

    for h in hexadecimal:
        if h=='a':
            decimal += 10*(16**exponente)
        elif h=='b':
            decimal += 11*(16**exponente)
        elif h=='c':
            decimal += 12*(16**exponente)
        elif h=='d':
            decimal += 13*(16**exponente)
        elif h=='e':
            decimal += 14*(16**exponente)
        elif h=='f':
            decimal += 15*(16**exponente)
        else:
            decimal += int(h)*(16**exponente)
        
        exponente -= 1

    print(f" >> El número {hexadecimal} en formato hexadecimal se corresponde con el número {decimal} en formato decimal.")



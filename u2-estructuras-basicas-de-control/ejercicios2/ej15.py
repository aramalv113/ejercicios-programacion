while True:
    try:
        contador = 0

        dividendo = int(input("Introduce el dividendo: "))
        divisor = int(input("Introduce el divisor: "))
        
        if divisor==0:
            print("No se puede dividir por 0.\n")
            continue

        dividendo = dividendo - divisor

        while dividendo >= 0:
            contador = contador + 1
            dividendo = dividendo - divisor
            
        print("El resultado es: " + str(contador) + "\n")
    
    except ValueError:
        print("No has introducido un dato numérico.\n")


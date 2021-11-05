while True:
    try:
        numeros = 1
        div = 1
        sumaDiv = 0
        n = int(input("Introduce un número: "))
        
        if n<=0:
            print("Por favor, introduce un número mayor a 0.")
            continue
        
        print("La lista de números perfectos anteriores al " + str(n) + " es: ")
        while numeros!=n:
            while div!=numeros:
                if numeros%div==0:
                    sumaDiv += div
                
                div += 1
            
            if sumaDiv==numeros:
                print(numeros, end=" ")
            
            numeros += 1
            div = 1
            sumaDiv = 0
        
        break
        
    except ValueError:
        print("No has introducido un dato numérico.")

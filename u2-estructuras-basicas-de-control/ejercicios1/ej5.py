try:
    n1 = float(input("Introduce n1: "))
    n2 = float(input("Introduce n2: "))
    n3 = float(input("Introduce n3: "))
    mayor = n1

    if n2 > mayor:
        mayor = n2
    elif n3 > mayor:
        mayor = n3
        
    print ("El numero",mayor,"es el mayor entre",n1,n2,"y",n3)
    
except ValueError:
    print("No has introducido un dato numérico.");

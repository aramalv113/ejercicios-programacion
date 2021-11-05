try:
    mayor = float(input("Introduce n1: "))
    
    n = float(input("Introduce n2: "))
    
    if n > mayor:
        mayor = n
        
    n = float(input("Introduce n3: "))
    
    if n > mayor:
        mayor = n
    
    print("El mayor de los tres números es",mayor)
    
except ValueError:
    print ("No has introducido un dato numérico.")
try:
    n1 = int(input("Introduce n1: "))
    n2 = int(input("Introduce n2: "))
    sumDiv1 = 0 
    sumDiv2 = 0
    div = 1 
    
    # Calculamos el número de divisores de n1
    while div!=n1:
        if n1%div==0:
            sumDiv1 = sumDiv1 + div
            
        div += 1
        
    div = 1
        
    # Calculamos el número de divisores de n2
    while div!=n2:
        if n2%div==0:
            sumDiv2 = sumDiv2 + div
            
        div += 1
        
    if sumDiv1==n2 and sumDiv2==n1:
        print("Los números son amigos.")
    else:
        print("Los números no son amigos.")
    
except ValueError:
    print("No has introducido un dato numérico.")


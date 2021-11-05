while True:
    try:
        n = int(input("Introduce un número mayor que 2: "))
        div = 2
        
        if n<=2:
            print("Por favor, introduce un número mayor que 2.")
            continue
        
        while div!=n:
            if n%div==0:
                print(f"{n} = {n//div} * {div}")
                
            div += 1
        
        break
        
        
    except ValueError:
        print("No has introducido un dato numérico.")
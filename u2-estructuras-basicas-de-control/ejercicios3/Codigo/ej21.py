while True:
    try:
        distancia = float(input("Distancia a recorrer: "))
        if distancia<0:
            print("La distancia debe de ser superior a 0.")
            continue
        
        estancia = int(input("Días de estancia: "))
        kmPrice = 10
        ticketPrice = 0
        
        if distancia>800.0 and estancia>7:
            kmPrice = kmPrice - (kmPrice*0.3)
        
        print(f"El precio del ticket es de {distancia*kmPrice}€")
        break;
                
        
    except ValueError:
        print("No has introducido un dato numérico.")
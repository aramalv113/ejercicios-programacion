try:
    print ("Puntuacion\tCalificación")
    print (">= 0.9\t\tSobresaliente")
    print (">= 0.8\t\tNotable")
    print (">= 0.7\t\tBien")
    print (">= 0.6\t\tSuficiente")
    print ("<  0.6\t\tInsuficiente")
    pts = float(input("Introduce una puntuacion: "))


    if pts>0.0 and pts<1.0:
        if pts>=0.9:
            print ("Sobresaliente")
        elif pts>=0.8:
            print ("Notable")
        elif pts>=0.7:
            print ("Bien")
        elif pts>=0.6:
            print ("Suficiente")
        else:
            print ("Insuficiente")
    else:
        print ("El valor introducido está fuera del rango (0.0,1.0)")
        
except ValueError:
    print ("No has introducido un dato numérico.")
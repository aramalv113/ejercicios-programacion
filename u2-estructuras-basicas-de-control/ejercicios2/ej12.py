positivos = 0
negativos = 0
suma = 0
n = 1

while n!=0:
    try:
        n = int(input("Introduce un número distinto de 0: "))
        
        if n!=0:
            suma += n
            
            if n>0:
                positivos += 1
            else:
                negativos += 1            
        
    except ValueError:
        print("No has introducido un dato numérico.")

print("La suma total es " + str(suma))
print("Se han introducido " + str(positivos) + " positivos y " + str(negativos) + " negativos.")
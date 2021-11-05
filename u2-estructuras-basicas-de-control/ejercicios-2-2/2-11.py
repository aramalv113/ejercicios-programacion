n = 0
contador = 0
suma = 0

while contador<=50:    
    
    if n%2==0:
        if contador==50:
            print(str(n))
        else:
            print(str(n), end=", ")
        
        contador += 1
        suma += n
    
    n += 1
    
print("\nLa suma de los 50 primeros números pares es " + str(suma))

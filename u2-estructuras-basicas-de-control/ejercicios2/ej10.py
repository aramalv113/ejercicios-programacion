n = 0
contador = 0

while contador<=50:    
    
    if n%2==0:
        if contador==50:
            print(str(n))
        else:
            print(str(n), end=", ")
        
        contador += 1
    
    n += 1
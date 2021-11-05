n = ""
suma = 0
contador = 0
media = 0.0
maximo = 0.0
minimo = 0.0
   
while n!="fin":
    try:
        n = input("Introduce un número: ")
        
        if n!="fin":
            
            n = float(n)
            
            if contador==1:
                maximo = n
                minimo = n
            else:
                if n>maximo:
                    maximo = n
                
                if n<minimo:
                    minimo = n
                    
            suma += n;
            contador+=1
            media = suma/contador
    
    except ValueError:
        print("Incorrecto.")
        
        
print(suma,contador,round(media,2),maximo,minimo)
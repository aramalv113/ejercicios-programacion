n = ""
suma = 0
contador = 0
media = 0.0
   
while n!="fin":
    try:
        n = input("Introduce un número: ")
        
        if n!="fin":
            suma += float(n);
            contador+=1
            media = suma/contador
    
    except ValueError:
        print("Incorrecto.")
        
        
print(suma,contador,media)    
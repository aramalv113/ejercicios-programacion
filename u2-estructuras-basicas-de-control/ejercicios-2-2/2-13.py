inicio = 1

try:
    n = int(input("Introduce un número entero: "))
    
    while inicio!=n and inicio!=-n:
        if inicio%2==0:
            print(-inicio, end=", ")
        else:
            print(inicio, end=", ")
            
        inicio += 1
        
    if n>0:
        if n%2==0:
            print(-n, end="")
        else:
            print(n, end="")
    else:
        if n%2==0:
            print(n, end="")
        else:
            print(n, end="")
        

except ValueError:
    print("No has introducido un dato numérico.")
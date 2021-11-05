try:
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    n3 = float(input("n3: "))
    mayor = n1
    menor = n1
    medio = None

    # Un bucle que recorre los tres número para identificar mayor y menor
    # de forma que conozcamos los dos extremos
    for vez in [n1,n2,n3]:
        if vez > mayor:
            mayor = vez
        elif vez < menor:
            menor = vez

    # Luego este bucle compara cada número con ambos extremos para ver si está
    # en el medio
    for vez in [n1,n2,n3]:
        if vez!=mayor and vez!=menor:
            medio = vez
            
    if medio:
        print ("El valor central es " + str(medio))
    else:
        print ("No ha sido posible encontrar el valor central.")
except ValueError:
    print("No has introducido un dato numérico.")
try:
    n1 = float(input("Introduce n1: "))
    n2 = float(input("Introduce n2: "))
    resultado = 0.0
    
    print("SUMAR -> '+'")
    print("RESTAR -> '-'")
    print("MULTIPLICAR -> '*'")
    print("DIVIDIR -> '/'")
    operacion = input("Qué operacion quieres hacer? >> ")
    
    if operacion=='+':
        print("Resultado >> ",str(n1+n2))
    elif operacion=='-':
        print("Resultado >> ",str(n1-n2))
    elif operacion=='*':
        print("Resultado >> ",str(n1*n2))
    elif operacion=='/':
        print("Resultado >> ",str(n1/n2))
    else:
        print("Has introducido un carácter incorrecto.")
    
except ValueError:
    print("No has introducido un dato numérico.")
altura = None # esta variable es la que guarda la altura que introducimos en el input
cont1 = 0 # cuenta los alumnos con altura mayor a 1.7 (no incluido)
cont2 = 0 # cuenta los alumnos con altura entre 1.6 (no incluido) y 1.7 (incluido)
cont3 = 0 # cuenta los alumnos con altura entre 1.5 (no incluido) y 1.6 (incluido)
cont4 = 0 # cuenta los alumnos más bajos de 1.5 (incluido)

while True:
    try:
        altura = float(input("Introduce altura del alumno: "))
        while altura!=0.0:
            if altura>1.7:
                cont1 += 1
            elif altura>1.6 and altura<=1.7:
                cont2 += 1
            elif altura>1.5 and altura<=1.6:
                cont3 += 1
            elif altura<=1.5 and altura>0:
                cont4 += 1
            else:
                print("Por favor, introduce una cantidad positiva.")
                
            altura = float(input("Introduce altura del alumno: "))
            
        print("Tabla de resultados\n");
        print(f"Hay {cont1} alumnos más altos que 1.70m")
        print(f"Hay {cont2} alumnos entre 1.60m y 1.70m")
        print(f"Hay {cont3} alumnos entre 1.60m y 1.50m")
        print(f"Hay {cont4} alumnos más bajos que 1.50m")
        break
    
    except:
        print("No has introducido una cantidad numérica.")
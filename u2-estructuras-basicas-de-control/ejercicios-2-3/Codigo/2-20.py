cont = 0
raizDefecto = 0
raizExceso = 0
raizUsuario = int(input("Introduce la raíz cuadrada: "))

while True:
    if cont*cont < raizUsuario:
        raizDefecto = cont
        cont += 1
    else:
        raizExceso = cont
        break

print("La raiz cuadrada de " + str(raizUsuario) + " está entre " + str(raizDefecto) + " y " + str(raizExceso))



        
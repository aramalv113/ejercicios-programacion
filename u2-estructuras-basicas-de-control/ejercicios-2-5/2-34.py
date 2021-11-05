import os

os.system("cls")

cantidadTotal = float(input("Introduce la cantidad total de dinero: "))
copiaCantidad = cantidadTotal
billetes = []
cantidades = []
veces = 0

for n in (500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01): # lista de todos los billetes y monedas disponibles
    # comprobamos si al dividir el dinero entre cada tipo es mayor a 1 el cociente, pues en caso de serlo 
    # significa que la cantidad de dinero cabe en ese tipo de billete o moneda
    # Tras comprobarlo, si la cantidad cabe en el billete o moneda, metemos el billete en la lista de billetes
    # y el cociente de dividir la cantidad entre el billete o moneda será las veces que cabe, por lo que también
    # lo guardamos en la lista de cantidades
    # 
    # en la variable veces guardamos una copia de las veces que cabe el dinero en ese tipo de billete o moneda para
    # restarlo a la cantidad total, por ejemplo, sin tenemos 230€, entonces tendremos que restarle 1 billete de 200
    # quedandonos para la siguiente vuelta 30€... y así sucesivamente
    if copiaCantidad/n>=1: 
        cantidades.append(int(copiaCantidad//n)) # cantidades.append(copiaCantidad//n) por qué no me guarda la división entera
        billetes.append(n)
        veces = int(copiaCantidad/n)

        copiaCantidad -= (veces*n) # cuando meto cualquier cantidad con 7 céntimos, se come 1 céntimo (?)

i = 0
print("Te corresponden: ")
while i<len(billetes): # también podría coger len(cantidades) ya que ambas medirán lo mismo
    print(f"- {cantidades[i]}",end="")
    if billetes[i] in (500,200,100,50,20,10,5):
        print(" billete",end="")
    else:
        print(" moneda",end="")
    
    if cantidades[i]>1:
            print("s",end="")
  
    print(f" de {billetes[i]}")

    i += 1
import os, random

os.system("cls")


def adivina_numero (num1:int,num2:int) -> int:
    """Comprueba si un numero es igual a otro

    Args:
        usuario (int): numero que introduce el usuario
        acertar (int): numero generado aleatoriamente

    Returns:
        int:
            0 si usuario es igual que acertar
            1 si usuario está a distacia de 2 de acertar
            2 si usuario es mayor que acertar
            3 si usuario es menor que acertar
        None:
            si recibe un parámetro no legal
    """
    try:
        diferencia = abs(num1 - num2)

        if diferencia<=2 and diferencia!=0:
            return 1
        elif num1>num2:
            return 2
        elif num1<num2:
            return 3
        
        return 0
    except TypeError:
        return None



if __name__=="__main__":
    vidas = 5
    inf_limit = 0
    sup_limit = 100

    acertar = random.randint(inf_limit,sup_limit)

    print(acertar)

    while vidas>0:
        
        print(f"Tienes {vidas} vida",end="")
        
        if vidas>1:
            print("s",end="")
        
        print("")

        usuario = int(input("Introduce un numero: "))

        result = adivina_numero(usuario,acertar)

        if result==0:
            print(f"HAS ACERTADO!! El numero era {acertar}")
            break
        else:
            print("LASTIMA!! Sigue intentandolo.")
            vidas -= 1

            match(result):
                case 1:
                    print("El número está muy cerca.")
                case 2: 
                    print("Un poco más abajo")
                case 3:
                    print("Un poco más arriba")

    if vidas==0:
        print(f"El numero era {acertar}")
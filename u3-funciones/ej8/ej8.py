import os

os.system("cls")



def num_digitos_binarios (d: int):
    """Calcula la cantidad de dígitos binarios (bits) necesarios para representar un número decimal

    Args:
        d (int): número en formato decimal

    Returns:
        int: cantidad de dígitos
        None: en caso de que se reciba un parámetro ilegal
    """
    try:
        digitos = 0

        if d >= 0:
            digitos = 1 
            cociente = d

            while cociente>=2:
                digitos += 1
                cociente = cociente//2

        return digitos
    except TypeError or ValueError:
        return None



if __name__=="__main__":
    decimal = 3

    print(num_digitos_binarios(decimal))


    d = None

    if d is None:
        print("hola")
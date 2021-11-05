import os

os.system("cls")



def esBisiesto (year: int=0) -> bool:
    """Comprueba si un año es bisiesto o no

    Args:
        year (entero, opcional): año a evaluar. Si no se recibe nada, por defecto es 0.

    Returns:
        bool: 
            True si el año es bisiesto
            False si el año no es bisiesto
    """
    try:
        if year>=0:
            if year%4==0 and year%100!=0 or year%400==0:
                return True
            else:
                return False
    except TypeError:
        return None



def compruebaFecha (dia: int=0, mes: int=0, anio: int=0) -> bool:
    """Comprueba si la fecha introducida es correcta o no.

    Args:
        dia (int, optional): por defecto es 0.
        mes (int, optional): por defecto es 0.
        anio (int, optional): por defecto 0.

    Returns:
        bool: 
            True si la fecha es correcta
            False si la fecha no es correcta
            None para parámetros no legales
    """
    try:
        mes31 = (1,3,5,7,8,10,12)
        mes30 = (4,6,9,11)

        if dia>=1 and mes>=1 and anio>=1:
            if (mes in mes31 and dia<=31) or (mes in mes30 and dia<=30) or (esBisiesto(anio) and dia<=29) or (dia<=28):
                return True

        return False
    except TypeError:
        return None



if __name__=="__main__":
    while True: 
        try:
            dia = int(input("Dia: "))
            mes = int(input("Mes: "))
            anio = int(input("Año: "))

            print(f"La fecha {dia}/{mes}/{anio}",end=" ")
            if not(compruebaFecha(dia,mes,anio)):
                print("no",end=" ")
            print("es correcta.")

            break

        except ValueError:
            print("Has introducido un dato no numérico.")
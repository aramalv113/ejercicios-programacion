import os
from ej6 import compruebaFecha

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



def cuentaDias (day:int, month:int, year:int) -> int:

    d = -1

    if compruebaFecha(day,month,year):
        d = 0
        m = 1

        while m<month:
            if m in (1,3,5,7,8,10,12):
                d += 31
            elif m in (4,6,9,11):
                d += 30
            else:
                if esBisiesto(year):
                    d += 29
                else:
                    d += 28
            
            m += 1
        
        d += day
    
    return d


def calcula_anio_completo(d1: int, d2: int, m1: int, m2: int, a1: int, a2: int) -> int:
    # 1 1 2020
    # 1 1 2021
    pass





if __name__=="__main__":
    fecha1 = input("Fecha 1:")
    #d1 = int(input("   Dia: "))
    #m1 = int(input("   Mes: "))
    #a1 = int(input("   Año: "))

    fecha2 = input("Fecha 2:")
    #d2 = int(input("   Dia: "))
    #m2 = int(input("   Mes: "))
    #a2 = int(input("   Año: "))

    #calcula_anio_completo(d1,d2,m1,m2,a1,a2)

    print(fecha1-fecha2)

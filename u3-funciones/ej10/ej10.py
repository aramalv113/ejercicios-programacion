
import os


os.system("cls")



# Esta función está testeada en "ej5"
def esBisiesto (year: int=0) -> bool:
    """Comprueba si un año es bisiesto o no

    Args:
        year (entero, opcional): año a evaluar. Si no se recibe nada, por defecto es 0.

    Returns:
        bool: 
            True si el año es bisiesto
            False si el año no es bisiesto
        None:
            si el parámetro es ilegal
    """
    try:
        if year>=0:
            if year%4==0 and year%100!=0 or year%400==0:
                return True
            else:
                return False
    except TypeError:
        return None



# Esta función está testeada en "ej6"
def compruebaFecha (dia: int, mes: int, anio: int) -> bool:
    """Comprueba si la fecha introducida es correcta o no.

    Args:
        dia (int)
        mes (int)
        anio (int)

    Returns:
        bool: 
            True si la fecha es correcta
            False si la fecha no es correcta
            None para parámetros no legales
    """
    try:
        mes31 = (1,3,5,7,8,10,12) # lista con los meses que tienen 31 días
        mes30 = (4,6,9,11) # lista con los meses que tienen 30 días

        if dia>=1 and mes>=1 and anio>=1:
            if (mes in mes31 and dia<=31) or (mes in mes30 and dia<=30) or (esBisiesto(anio) and dia<=29) or (dia<=28):
                return True

        return False
    except TypeError:
        return None


     
def convierte_en_dias (day:int, month:int, year:int) -> int:
    """Convierte en días una fecha

    Args:
        day (int)
        month (int)
        year (int)

    Returns:
        int: 
            número de días en los que se convierte la fecha
            -1 si la fecha introducida no es correcta
            None si se recibe algún parámetro ilegal
    """
    d = -1

    comp = compruebaFecha(day,month,year)

    if comp is True:
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
    elif comp is None:
        return None
    
    return d



def calcula_anio_completo(d1: int, m1: int, a1: int, d2: int, m2: int, a2: int):
    """Calcula los años completos que hay entre dos fechas

    Args:
        d1 (int): dia de fecha 1
        m1 (int): mes de fecha 1
        a1 (int): año de fecha 1
        d2 (int): dia de fecha 2
        m2 (int): mes de fecha 2
        a2 (int): año de fecha 2

    Returns:
        int:
            cantidad de años completos entre las fechas
            -1 si alguna de las fechas, o ambas, es incorrecta
            None si se introducen parámetros ilegales
    """
    years = -1
    # Calculamos los días que hay desde d1/m1/a1 hasta el 31 de diciembre de ese año (a1)
    diasFecha1 = convierte_en_dias(d1,m1,a1)
    # Calculamos los días que hay desde el 1 de enero del año a2 hasta la d2/m2/a2
    diasFecha2 = convierte_en_dias(d2,m2,a2)

    # Si ambos nos devuelven algo distinto a -1, las fechas están correctas y podemos continuar
    if (diasFecha1 is None) or (diasFecha2 is None):
        years = None
    elif diasFecha1!=-1 and diasFecha2!=-1:
        # -- le restamos 366 días a los días que han pasado desde el 1 de enero hasta d1 si es bisiesto
        # -- le restamos 365 días a los días que han pasado desde el 1 de enero hasta d1 si no es bisiesto
        if esBisiesto(a1):
            diasFecha1 = abs(diasFecha1 - 366)        
        else:
            diasFecha1 = abs(diasFecha1 - 365)

        # Detectamos el año menor entre los dos para comenzar a contar los años completos que hay
        if a1<a2:
            inicio = a1 + 1
            fin = a2
        else:
            inicio = a2 + 1
            fin = a1

        years = (fin - inicio) + ((diasFecha1 + diasFecha2)//365)
    

    return years



if __name__=="__main__":
    print("Fecha nacimiento:")
    d1 = int(input("   Dia: "))
    m1 = int(input("   Mes: "))
    a1 = int(input("   Año: "))

    print("\n")

    print("Fecha actual:")
    d2 = int(input("   Dia: "))
    m2 = int(input("   Mes: "))
    a2 = int(input("   Año: "))

    years = (calcula_anio_completo(d1,m1,a1,d2,m2,a2)>=18)

    print("Eres mayor de edad.") if years else print("No eres mayor de edad.")
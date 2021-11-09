import os

os.system("cls")



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



def calcula_anio_completo(d1: int, m1: int, a1: int, d2: int, m2: int, a2: int) -> int:
    # Primero calculamos los días que hay entre la fecha 1 (d1/m1/a1) hasta el 31 de diciembre de ese mismo año y
    # -- le restamos 366 días a los días que han pasado desde el 1 de enero hasta d1 si es bisiesto
    # -- le restamos 365 días a los días que han pasado desde el 1 de enero hasta d1 si no es bisiesto
    diasFecha1 = convierte_en_dias(d1,m1,a1)
    if esBisiesto(a1):
        diasFecha1 = abs(diasFecha1 - 366)         
    else:
        diasFecha1 = abs(diasFecha1 - 365)
        

    # Segundo calculamos los días transcurridos que hay entre el 1 de enero y la fecha 2 (d2/m2/a2)
    diasFecha2 = convierte_en_dias(d2,m2,a2)

    # Tercero calculamos los dias transcurridos entre los años a1 y a2. Para ello, tenemos que comenzar a contar desde el año siguiente
    # al año menor entre los dos. Es decir, si nos pasan 1/1/2029 y 1/1/2020, empezaremos a contar desde el 2021 hasta el 2029 (sin contar)# ya que en los pasos anteriores ya hemos calculado los días que hay fuera de estos años.
    diasEntreAnios = 0

    # Antes tenemos que ver desde qué año empezamos, comprobando cuál es el menor. En caso 
    if a1<a2:
        inicio = a1 + 1
        fin = a2
    else:
        inicio = a2 + 1
        fin = a1

    anios = (fin - inicio) + ((diasFecha1 + diasFecha2)//365)

    return anios



if __name__=="__main__":
    #fecha1 = input("Fecha 1:")
    #d1 = int(input("   Dia: "))
    #m1 = int(input("   Mes: "))
    #a1 = int(input("   Año: "))

    #fecha2 = input("Fecha 2:")
    #d2 = int(input("   Dia: "))
    #m2 = int(input("   Mes: "))
    #a2 = int(input("   Año: "))

    #calcula_anio_completo(d1,d2,m1,m2,a1,a2)

    #print(fecha1-fecha2)

    pass

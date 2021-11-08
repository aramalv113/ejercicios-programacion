import os

os.system("cls")



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



def calcula_anio_completo(d1: int, m1: int, a1: int, d2: int, m2: int, a2: int) -> int:
    # 1 1 2020
    # 1 1 2021

    # si los años son distintos, podremos hacer el cálculo, de lo contrario, estaríamos en el mismo año y no habría pasado ningún año completo
    if a1!=a2:

        # Primero calculamos los días que hay entre la fecha 1 (d1/m1/a1) hasta el 31 de diciembre de ese mismo año esto dependerá de si el año # es bisiesto o no:
        # -- le restamos 366 días a los días que han pasado desde el 1 de enero hasta d1 si es bisiesto
        # -- le restamos 365 días a los días que han pasado desde el 1 de enero hasta d1 si no es bisiesto
        # cuentaDias() nos da el numero de días transcurridos entre el 1 de enero y d1
        diasFecha1 = cuentaDias(d1,m1,a1)
        if esBisiesto(a1):
            diasFecha1 = abs(diasFecha1 - 366)         
        else:
            diasFecha1 = abs(diasFecha1 - 365)
        

        # Segundo calculamos los días transcurridos que hay entre el 1 de enero y la fecha 2 (d2/m2/a2)
        diasFecha2 = cuentaDias(d2,m2,a2)

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

        # con este bucle vamos acumulando los días entre los años
        while inicio<fin:
            diasEntreAnios += cuentaDias(31,12,inicio)

            inicio += 1        

        # Por último, sumamos todos los datos que tenemos
        diasTotales = diasFecha1 + diasFecha2 + diasEntreAnios

        return diasTotales//365
    
    return 0



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

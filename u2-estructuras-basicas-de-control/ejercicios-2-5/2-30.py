import os

def esBisiesto (year: int):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    
    return False

def compruebaFecha(d:int,m:int,y:int):
    if m in (1,3,5,7,8,10,12) and d>31 or d>30:
        return False
    elif (m==2 and esBisiesto(y) and d>29) or d>28:
        return False

    return True

def convierteEnDias (d:int, m:int, y:int):
    i = 1
    totalDays = 0
        
    while i < m:
        if i in (1,3,5,7,8,10,12):
            totalDays = totalDays + 31
        elif i in (4,6,9,11):
            totalDays = totalDays + 30
        else:
            if esBisiesto(year):
                totalDays = totalDays + 29
            else:
                totalDays = totalDays + 28
        
        i = i + 1
    
    totalDays = totalDays + d
        
    return totalDays

while True:
    if __name__ == "__main__":
        
        os.system("cls")

        day = int(input("Día: "))
        month = int(input("Mes: "))
        year = int(input("Año: "))
        start = 0
        
        if compruebaFecha(day,month,year):
            print(f"Muy bien! Tu fecha es {day}/{month}/{year}\n")
        else:
            print(f" >> Error: la fecha {day}/{month}/{year} no es correcta.")
            continue
        
        weekDay = int(input(f"1. Lunes\n2. Martes\n3. Miércoles\n4. Jueves\n5. Viernes\n6. Sábado\n7. Domingo.\nElige el día de la semana al que corresponde el 1 de enero del año {year}: "))
        
        while weekDay<1 or weekDay>7:
            print(f"Muy bien! Tu fecha es: {day}/{month}/{year}\n")
            print(f" >> {weekDay} no se corresponde con ninguna de las opciones. Por favor, inténtalo de nuevo.\n")
            weekDay = int(input(f"1. Lunes\n2. Martes\n3. Miércoles\n4. Jueves\n5. Viernes\n6. Sábado\n7. Domingo.\nElige el día de la semana al que corresponde el 1 de enero del año {year}: "))
        
        # le resto al total de días de la semana el número que corresponda al día
        # también le sumo 1 porque para el programa el lunes empieza en 0 y no en 1 como elige el usuario
        start = convierteEnDias(day,month,year) - (7 - weekDay + 1)
        
        weekDay2 = int(start % 7)

        print(" >> cae en ",end="")
        if weekDay2==0:
            print("domingo")
        elif weekDay2==1:
            print("lunes")
        elif weekDay2==2:
            print("martes")
        elif weekDay2==3:
            print("miércoles")
        elif weekDay2==4:
            print("jueves")
        elif weekDay2==5:
            print("viernes")
        elif weekDay2==6:
            print("sábado")
        
        break
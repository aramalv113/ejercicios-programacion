# Introducir por teclado la fecha actual y la fecha de nacimiento del usuario (día, mes y año) e indicar si es mayor
# de 20 años.

# 1 año = 31557600 Segundos, 1 mes = 2629800 Segundos, 1 día = 86400 Segundos
def aSegundos (d:int,m:int,y:int):
    return d*86400+m*2629800+y*31557600

def toYears (s:int):
    return s//31557600

def pedirFecha(mensaje:str):
    try:
        print(mensaje)
        day = int(input("Día: "))
        while day<1 or day>31:
            print(" >> Debes introducir una cantidad comprendida entre 1 y 31.")
            day = int(input("Día: "))
        month = int(input("Mes: "))
        while month<1 or month>12:
            print(" >> Debes introducir una cantidad comprendida entre 1 y 12.")
            month = int(input("Mes: "))
        year = int(input("Año: "))
        while year<1:
            print(" >> Debes introducir una cantidad superior a 1.")
            year = int(input("Año: "))

        return aSegundos(day,month,year)
    except ValueError:
        print("Por favor, introduce un dato numérico.")

def comprobar (a:int, b:int):
    if abs(toYears(a)-toYears(b))-18>=0:
        print(" >> Eres mayor de edad.")
        print(f" >> Tienes {toYears(abs(a-b))} años.")
    else:
        print(" >> No eres mayor de edad.")
        print(f" >> Te faltan {abs(toYears(abs(a-b))-18)} años.")

if __name__=="__main__":
    current = pedirFecha("Fecha actual:")
    user = pedirFecha("Fecha de nacimiento:")

    comprobar(current,user)
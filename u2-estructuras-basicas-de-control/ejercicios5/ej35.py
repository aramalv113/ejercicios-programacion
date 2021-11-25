import os
os.system("cls")

mes = int(input("Introduce un mes del año: "))
while mes < 1 and mes > 12:
    print(" >> el mes solo puede ser un valor comprendido entre 1 y 12.\n")
    mes = int(input("Introduce un mes del año: "))

weekDay = int(input(
    "1. Lunes\n2. Martes\n3. Miércoles\n4. Jueves\n5. Viernes\n6. Sábado\n7. Domingo.\nElige el día de la semana en el que empieza el mes: "))

if mes in (1,3,5,7,8,10,12):
    dias = 31
elif mes in(4,6,9,11):
    dias = 30
else:
    dias = 28

print("LU MA MI JU VI SA DO\n")
print(" "*(3*(weekDay-1)),end="")

d = weekDay
contador = 1
while contador<=dias:
    print("%.2d "%contador,end="")
    
    if d==7: 
        print("\n")
        d=0

    d += 1
    contador += 1
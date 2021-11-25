# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total
# del servicio.

work_hours = int(input("Horas trabajadas: "))
hour_price = int(input("Coste por hora: "))
salary = work_hours * hour_price;

print ("Importe total: " + str(salary))
total_hours = float(input("Horas trabajadas: "))
price = float(input("Precio por hora: "))
salary = 0.0
plus_hours = 0

if total_hours >= 40:
    plus_hours = total_hours - 40

salary = (plus_hours*1.5*price) + ((total_hours-plus_hours) * price)

print ("Salario total:",salary)
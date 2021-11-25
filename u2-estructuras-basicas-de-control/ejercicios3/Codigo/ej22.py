while True:
    day = None
    month = None
    year = None
    
    try:
        day = int(input("Día: "))
        if day<=0 or day>31:
            print("'Días' debe estar entre 1 y 31.")
            continue
        
        month = int(input("Mes: "))
        if month<=0 or month>12:
            print("'Mes' debe estar entre 1 y 12.")
            continue
        
        year = int(input("Año: "))
        if year<=0:
            print("'Año' debe ser una cantidad superior a 0.")
            continue
        
        day+=1
        if month!=2:
            if ((month==4 or month==6 or month==9 or month==11) and day>30) or day>31:
                day=1
                month+=1
                if month>12:
                    month=13
                    year+=1
        else:
            if (((year%4==0 and year%100!=0) or year%400!=0) and day>28) or day>29:
                day=1
                month+=1
                     
        print(day,month,year)
        break   
        
    except ValueError:
        print("No has introducido un dato numérico.")
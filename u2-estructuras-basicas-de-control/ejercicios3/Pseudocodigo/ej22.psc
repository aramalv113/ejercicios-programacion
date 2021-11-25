Algoritmo diaSiguiente
	Escribir "Dia: "
	Leer day
	Mientras day<=0 | day>31 Hacer
		Escribir "El día debe estar entre 1 y 31."
		Escribir "Dia: "
		Leer day
	FinMientras
	
	Escribir "Mes: "
	Leer month
	Mientras month<=0 | month>12 Hacer
		Escribir "El mes debe estar entre 1 y 12."
		Escribir "Mes: "
		Leer month
	FinMientras
	
	Escribir "Año: "
	Leer year
	Mientras year<=0 Hacer
		Escribir "El año debe ser mayor a 0."
		Escribir "Año: "
		Leer year
	FinMientras
	
	day<-day+1
	Si month<>2 Entonces
		si ((month==4 | month==6 | month==9 | month==11) & day>30) | day>31 Entonces
			day<-1
			month<-month+1
			Si month>12 Entonces
				month<-1
				year<-year+1
			FinSi
		FinSi
	SiNo
		Si (((year%4==0 & year%100<>0) | year%400<>0) & day>28) | day>29 Entonces
			day<-1
			month<-month+1
		FinSi
	FinSi
		
	Escribir day,"/",month,"/",year
FinAlgoritmo

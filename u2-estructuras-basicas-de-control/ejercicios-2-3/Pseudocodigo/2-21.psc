Algoritmo precioTicket

	Escribir "Distancia a recorrer: "
	Leer distancia
		
	Mientras distancia<=0 Hacer
		Escribir "Distancia debe ser mayor a 0."
		Escribir "Distancia a recorrer: "
		Leer distancia
	FinMientras
		
	Escribir "Días de estancia: "
	Leer estancia
		
	Mientras estancia<0 Hacer
		Escribir "Estancia no puede ser negativa."
		Escribir "Días de estancia:  "
		Leer estancia
	FinMientras
		
	kmPrice<-10
		
	Si distancia>800.0 & estancia>7 Entonces
		kmPrice<-kmPrice - (kmPrice*0.3)
	FinSi
		
	Escribir "El precio del ticket es de ",kmPrice*distancia," euros."
FinAlgoritmo

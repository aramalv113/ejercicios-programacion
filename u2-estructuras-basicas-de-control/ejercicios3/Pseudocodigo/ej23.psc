Algoritmo AlturasClase
	cont1<-0
	cont2<-0
	cont3<-0
	cont4<-0
	
	Escribir "Introduce la altura del alumno: "
	Leer altura
	
	Mientras altura<>0 Hacer
		Si altura>1.7 Entonces
			cont1<-cont1+1
		SiNo
			Si altura>1.6 & altura<=1.7 Entonces
				cont2<-cont2+1
			SiNo
				Si altura>1.5 & altura<=1.6 Entonces
					cont3<-cont3+1
				SiNo
					Si altura<=1.5 & altura>0 Entonces
						cont4<-cont4+1
					SiNo
						Escribir "Por facor, introduce una altura mayor a 0."
					FinSi
				FinSi
			FinSi
		FinSi
		
		Escribir "Introduce la altura del alumno: "
		Leer altura
	FinMientras
	
	Escribir "Tabla de resultados\n"
	Escribir "Hay ",cont1," alumnos más altos que 1.70m"
	Escribir "Hay ",cont2," alumnos entre 1.60m y 1.70m"
	Escribir "Hay ",cont3," alumnos entre 1.50m y 1.60m"
	Escribir "Hay ",cont4," alumnos más bajos que 1.50m"
FinAlgoritmo

Algoritmo ValorCentral
	Escribir "Introduce n1: "
	Leer n1
	Escribir "Introduce n2: "
	Leer n2
	Escribir "Introduce n3: "
	Leer n3
	
	mayor<-n1
	menor<-n2
	medio<-None
	
	Si n1>n2 && n1<n3 Entonces
		medio = n1
	SiNo
		Si n2>n1 && n2<n3 Entonces
			medio = n2
		SiNo
			Si n3>n1 && n3<n2 Entonces
				medio = n3
			Fin Si
		Fin Si
	Fin Si
	
	Si medio<>None Entonces
		Escribir "El valor central es ", medio
	SiNo
		Escribir "No ha sido posible encontrar el valor central."
	FinSi
FinAlgoritmo

Algoritmo RaizPorAproximacion
	cont<-0
	raizDefecto<-0
	raizExceso<-0
	
	Escribir "Introduce la raiz cuadrada: "
	Leer raizUsuario
	
	Mientras cont*cont < raizUsuario Hacer
		raizDefecto<-cont
		cont<-cont+1
	Fin Mientras
	
	raizExceso<-cont
	
	Escribir "La raiz cuadrada de ",raizUsuario," está entre ",raizDefecto," y ",raizExceso
FinAlgoritmo

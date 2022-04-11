Algoritmo angulos
	Definir angulo1 Como Entero
	Definir angulo2 Como Entero
	Definir angulo3 Como Entero
	
	Escribir "Ingrese angulo 1"
	leer angulo1
	Escribir "Ingrese angulo 2"
	leer angulo2
	Escribir "Ingrese angulo 3"
	leer angulo3
	
	si angulo1 = angulo2 y angulo1 = angulo3 Entonces
		Escribir "equilatero"
	SiNo
		si angulo1 = angulo2 o angulo1 = angulo3 o angulo2 = angulo3 Entonces
			Escribir "Isoceles"
		SiNo
			Escribir "Escaleno"
			
		FinSi
	FinSi
	
FinAlgoritmo

Algoritmo Descuentos
	
	Definir totalCompra Como Entero
	Definir totalAPagar Como Real
	
	Escribir "Ingrese total de la compra"
	Leer totalCompra
	
	si totalCompra >= 500 Entonces
		totalAPagar = totalCompra * .7
	SiNo
		si totalCompra >= 200 Entonces
			totalAPagar = totalCompra * .8
		SiNo
			si totalCompra >= 100 Entonces
				totalAPagar = totalCompra * .9
			sino
				totalAPagar = totalCompra
			FinSi
		FinSi
	FinSi
	
	Escribir "El total a pagar es: ", totalAPagar
	
FinAlgoritmo

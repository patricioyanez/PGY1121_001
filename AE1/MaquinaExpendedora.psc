Algoritmo MaquinaVendedora
	// realizar la venta de 3 productos: Coca cola, Fanta y Sprite.
	//Los valores de estos son: 600, 500 y 350.[1 al 3]
	// solicitar al usuario que producto quiere y la cantidad.
	// mostrar el total a pagar.
	
	Definir opcion Como Entero
	Definir cantidad Como Entero
	Definir total Como Entero
	
	Escribir " ******  Super Máquina Vendedora *******"
	Escribir "1.- Coca cola $600"
	Escribir "2.- Fanta     $500"
	Escribir "3.- Sprite    $350"
	Escribir "Seleccione un producto:"
	Leer opcion
	Escribir "Indice la cantidad:"
	Leer cantidad
	
	si opcion = 1 Entonces
		total = cantidad * 600
	SiNo
		si opcion = 2 Entonces
			total = cantidad * 500
		SiNo
			total = cantidad * 350
		FinSi
	FinSi
	
	Escribir "El total a pagar es:", total
	
	
FinAlgoritmo

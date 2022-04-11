Algoritmo EjemploMientrasMenu
	Definir opcion Como Entero
	
	opcion = 0
	
	Mientras opcion <> 4 Hacer  // < >  o  ! =
		Limpiar Pantalla
		Escribir "******* Super menú *******"
		Escribir "1.- Saludar"
		Escribir "2.- Despedirse"
		Escribir "3.- otro"
		Escribir "4.- Salir"
		Escribir "Seleccione una opción"
		Leer opcion
		
		si opcion = 1 Entonces
			Escribir "Hola mamiii, te quero mucho!!! :)"
			Escribir "Presione cualquier tecla para continuar"
			//Esperar Tecla
			Esperar 3 Segundos
		FinSi
		
		si opcion = 2 Entonces
			Escribir "Chauuuu, nos vemos!!!"
			Escribir "Presione cualquier tecla para continuar"
			Esperar Tecla
		FinSi
		
	FinMientras
	Escribir "Aplicación cerrada"
	
FinAlgoritmo

def main():
	print("-------------------------------------------------------------------------------------")
	print("Bienvenido al manejador de tablas de métodos virtuales. Este trabaja sobre un sistema")
	print("orientado a objetos, con herencia simple y despacho dinámico de métodos.")
	print("\nIMPORTANTE: los nombres de tipos/métodos no pueden contener espaciosy se distingue")
	print("entre mayúsculas y minúsculas.\n")
	print("Comandos disponibles:")
	print("CLASS <tipo> [<nombre>] - crea una clase de tipo <tipo> con metodos [<nombre>]")
	print("CLASS <tipo> : <super> [<nombre>] - para crear una subclase de <super>")
	print("DESCRIBIR <tipo> - muestra la tabla de métodos virtuales de la clase <tipo>")
	print("SALIR - termina la ejecución del manejador")
	print("-------------------------------------------------------------------------------------\n")

	while True:
		entrada = input(">>> ").strip().split(" ")
		entrada = [entrada[0].upper()] + entrada[1:]

		match entrada:
			case ["SALIR"]:
				break

			case ["CLASS", tipo, ":", super, *metodos]:
				print("Se quiere crear una subclase de", super, "de tipo", tipo, "con los métodos", metodos)
			
			case ["CLASS", tipo, *metodos]:
				print("Se quiere crear una clase de tipo", tipo, "con los métodos", metodos)

			case ["DESCRIBIR", tipo]:
				print("Se quiere describir la clase de tipo", tipo)

			case ["CLASS", *_]:
				print("Usos del comando CLASS:")
				print("CLASS <tipo> [<nombre>] - crea una clase de tipo <tipo> con metodos [<nombre>]")
				print("CLASS <tipo> : <super> [<nombre>] - para crear una subclase de <super>")

			case ["DESCRIBIR", *_]:
				print("Uso del comando DESCRIBIR:")
				print("DESCRIBIR <tipo> - muestra la tabla de métodos virtuales de la clase <tipo>")

			case [""]:
				continue
			
			case _:
				print("Comando no reconocido.")

if __name__ == "__main__":
	main()
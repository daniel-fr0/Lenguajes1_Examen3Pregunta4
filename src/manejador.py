from src.Registro import Registro

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

	registro = Registro()

	while True:
		entrada = input(">>> ").strip().split(" ")
		entrada = [entrada[0].upper()] + entrada[1:]

		match entrada:
			case ["SALIR"]:
				break

			case ["CLASS", tipo, ":", super, *metodos]:
				try:
					registro.definir(tipo, metodos, super)
				except Exception as e:
					print(e)

			case ["CLASS", tipo, *metodos]:
				try:
					registro.definir(tipo, metodos)
				except Exception as e:
					print(e)

			case ["DESCRIBIR", tipo]:
				try:
					print("\n".join(registro.describir(tipo)))
				except Exception as e:
					print(e)

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
				print("Comando no reconocido")

if __name__ == "__main__":
	main()
from src.Clase import Clase

class Registro():
	def __init__(self):
		self.clases = {}

	def definir(self, tipo, metodos, padre=None):
		if tipo in self.clases:
			raise Exception("Clase ya definida")
		
		if padre and padre not in self.clases:
			raise Exception("Clase padre no definida")
		
		padre = self.clases[padre] if padre else None

		self.clases[tipo] = Clase(tipo, metodos, padre)
		return True
	
	def describir(self, tipo):
		if tipo not in self.clases:
			raise Exception("Clase no definida")
		desc = self.clases[tipo].descripcion()
		if len(desc) == 0:
			return ["No hay métodos definidos"]
		return desc
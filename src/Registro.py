from src.Clase import Clase

class Registro():
	def __init__(self):
		self.clases = {}

	def definir(self, tipo, metodos, padre=None):
		if tipo in self.clases:
			return False
		
		if padre and padre not in self.clases:
			return False
		
		padre = self.clases[padre] if padre else None
		self.clases[tipo] = Clase(tipo, metodos, padre)
		return True
	
	def describir(self, tipo):
		if tipo not in self.clases:
			return None
		return self.clases[tipo].descripcion()
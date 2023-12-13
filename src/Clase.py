class Clase():
	def __init__(self, tipo, metodos, padre=None):
		if dependencia_circular(tipo, padre):
			raise Exception('Dependencia circular detectada.')

		self.tipo = tipo
		self.padre = padre
		self.vtable = dict((metodo, tipo) for metodo in metodos)

		if padre:
			for metodo in padre.vtable:
				if metodo in self.vtable: continue
				self.vtable[metodo] = padre.vtable[metodo]

		self.metodos = sorted(self.vtable.keys())

	def descripcion(self):
		tabla = []
		for metodo in self.metodos:
			tabla.append(f'{metodo} -> {self.vtable[metodo]} :: {metodo}')
		return tabla


	def __str__(self):
		if self.padre:
			return f'{self.tipo} : {self.padre.tipo} -> {{{ ', '.join(self.metodos) }}}'
		return f"{self.tipo} -> {{{ ', '.join(self.metodos) }}}"
	
	def __expr__(self):
		return self.__str__()
	
def dependencia_circular(tipo, padre):
	if not padre: return False
	if tipo == padre.tipo: return True
	return dependencia_circular(tipo, padre.padre)
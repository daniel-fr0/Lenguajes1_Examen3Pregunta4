import unittest
from src.Clase import Clase

class TestClase(unittest.TestCase):
	def test_descripcion(self):
		A = Clase('A', ['f', 'g'])
		self.assertEqual(A.descripcion(), [
			'f -> A :: f',
			'g -> A :: g'
		])

	def test_herencia(self):
		A = Clase('A', ['f', 'g'])
		B = Clase('B', ['f', 'h'], A)
		self.assertEqual(B.descripcion(), [
			'f -> B :: f', 
			'g -> A :: g', 
			'h -> B :: h'
		])

	def test_abuelo(self):
		A = Clase('A', ['f', 'g'])
		B = Clase('B', ['f', 'h'], A)
		C = Clase('C', ['f', 'i'], B)
		self.assertEqual(C.descripcion(), [
			'f -> C :: f', 
			'g -> A :: g', 
			'h -> B :: h', 
			'i -> C :: i'
		])

	def test_dependencia_circular(self):
		A = Clase('A', ['f', 'g'])
		B = Clase('B', ['f', 'h'], A)
		C = Clase('C', ['f', 'i'], B)
		with self.assertRaises(Exception):
			Clase('A', ['f', 'g'], C)

	def test_str(self):
		A = Clase('A', ['f', 'g'])
		self.assertEqual(str(A), 'A -> {f, g}')
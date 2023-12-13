import unittest
from src.Registro import Registro

class TestRegistro(unittest.TestCase):
	def test_definir(self):
		registro = Registro()
		self.assertTrue(registro.definir('A', ['f', 'g']))
		self.assertTrue(registro.definir('B', ['f', 'h'], 'A'))
		self.assertTrue(registro.definir('C', ['f', 'i'], 'B'))
		with self.assertRaises(Exception):
			registro.definir('A', ['f', 'g'], 'C')
			registro.definir('D', ['f', 'j'], 'E')

	def test_describir(self):
		registro = Registro()
		registro.definir('A', ['f', 'g'])
		registro.definir('B', ['f', 'h'], 'A')
		registro.definir('C', ['f', 'i'], 'B')
		self.assertEqual(registro.describir('A'), [
			'f -> A :: f',
			'g -> A :: g'
		])
		self.assertEqual(registro.describir('B'), [
			'f -> B :: f',
			'g -> A :: g',
			'h -> B :: h'
		])
		self.assertEqual(registro.describir('C'), [
			'f -> C :: f',
			'g -> A :: g',
			'h -> B :: h',
			'i -> C :: i'
		])
		self.assertRaises(Exception, registro.describir, 'D')
import io
import unittest
from unittest.mock import patch
from src.manejador import main


class TestManejador(unittest.TestCase):
	def test_salir(self):
		with patch('builtins.input', side_effect=['SALIR']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[1], 'Bienvenido al manejador de tablas de métodos virtuales. Este trabaja sobre un sistema')

	def test_comando_desconocido(self):
		with patch('builtins.input', side_effect=['ejecutar', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], 'Comando no reconocido')

	def test_comando_vacio(self):
		with patch('builtins.input', side_effect=['', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '-------------------------------------------------------------------------------------')

	def test_crear_clase(self):
		with patch('builtins.input', side_effect=['class A', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '-------------------------------------------------------------------------------------')

	def test_crear_clase_con_super(self):
		with patch('builtins.input', side_effect=['class A', 'class B : A', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '-------------------------------------------------------------------------------------')

	def test_crear_clase_vacia(self):
		with patch('builtins.input', side_effect=['class A', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '-------------------------------------------------------------------------------------')
	
	def test_crear_clase_con_super_vacia(self):
		with patch('builtins.input', side_effect=['class A', 'class B : A', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '-------------------------------------------------------------------------------------')

	def test_describir_clase(self):
		commands = [
			'class A f g',
			'describir A',
			'salir'
		]
		expected = [
			'f -> A :: f',
			'g -> A :: g'
		]
		
		with patch('builtins.input', side_effect=commands):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				for i in range(len(expected)):
					self.assertEqual(output[i-len(expected)], expected[i])

	def test_describir_clase_con_super(self):
		commands = [
			'class A f g',
			'class B : A f h',
			'describir B',
			'salir'
		]
		expected = [
			'f -> B :: f',
			'g -> A :: g',
			'h -> B :: h'
		]
		
		with patch('builtins.input', side_effect=commands):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				for i in range(len(expected)):
					self.assertEqual(output[i-len(expected)], expected[i])

	def test_describir_clase_vacia(self):
		commands = [
			'class A',
			'class B : A',
			'describir A',
			'describir B',
			'salir'
		]
		expected = [
			'No hay métodos definidos',
			'No hay métodos definidos'
		]
		
		with patch('builtins.input', side_effect=commands):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				for i in range(len(expected)):
					self.assertEqual(output[i-len(expected)], expected[i])

	def test_describir_clase_vacia_con_super(self):
		commands = [
			'class A f g',
			'class B : A',
			'describir A',
			'describir B',
			'salir'
		]
		expected = [
			'f -> A :: f',
			'g -> A :: g',
			'f -> A :: f',
			'g -> A :: g',
		]
		
		with patch('builtins.input', side_effect=commands):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				for i in range(len(expected)):
					self.assertEqual(output[i-len(expected)], expected[i])

	def test_crear_clase_ya_definida(self):
		commands = [
			'class A f g',
			'class A f h',
			'salir'
		]
		expected = [
			'Clase ya definida'
		]
		
		with patch('builtins.input', side_effect=commands):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				for i in range(len(expected)):
					self.assertEqual(output[i-len(expected)], expected[i])

	def test_crear_clase_con_super_no_definido(self):
		commands = [
			'class A f g',
			'class B : C f h',
			'salir'
		]
		expected = [
			'Clase padre no definida'
		]
		
		with patch('builtins.input', side_effect=commands):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				for i in range(len(expected)):
					self.assertEqual(output[i-len(expected)], expected[i])

	def test_describir_clase_no_definida(self):
		commands = [
			'describir A',
			'salir'
		]
		expected = [
			'Clase no definida'
		]
		
		with patch('builtins.input', side_effect=commands):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				for i in range(len(expected)):
					self.assertEqual(output[i-len(expected)], expected[i])
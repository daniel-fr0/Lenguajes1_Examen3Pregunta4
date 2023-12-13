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
				self.assertEqual(output[-1], 'Comando no reconocido.')

	def test_comando_vacio(self):
		with patch('builtins.input', side_effect=['', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '-------------------------------------------------------------------------------------')
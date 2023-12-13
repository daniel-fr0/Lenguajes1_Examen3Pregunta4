import io
import unittest
from unittest.mock import patch
from src.manejador import main


class TestManejador(unittest.TestCase):
	def test_main(self):
		with patch('builtins.input', side_effect=['SALIR']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[1], 'Bienvenido al manejador de tablas de métodos virtuales. Este trabaja sobre un sistema')
# Manejador de tablas de métodos virtuales

Este proyecto implementa un programa que permite manejar tablas de métodos virtuales para un sistema orientado a objetos. 
El sistema permite la herencia simple y sobrecarga de métodos.
Se pueden definir clases y consultar la tabla de métodos virtuales sobre las clases que se definan.
El programa fue desarrollado en Python `3.12.1` y utiliza características de la versión `3.10` del lenguaje.

## Ejecución del programa principal

Para ejecutar el programa se debe ejecutar el archivo `main.py` con Python 3.10 o superior.
El programa se ejecuta de la siguiente manera:

```bash
	python main.py
```

## Ejecución de los tests

Para ejecutar los tests se cuenta con el script `run_tests.sh` que ejecuta todos los tests del proyecto.
Tambien se pueden ejecutar con el siguiente comando en el directorio raíz del proyecto:

```bash
	python -m unittest discover -s tests -v
```
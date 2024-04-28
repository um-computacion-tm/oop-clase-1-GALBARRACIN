# Importamos la biblioteca unittest para poder escribir tests unitarios
import unittest

# Definimos la clase Alumno, que será utilizada más adelante en los tests
class Alumno:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo

# Definimos la clase Materia
class Materia:
    def __init__(self, nombre, profesores):
        # Inicializamos los atributos nombre y profesores de la materia
        self.nombre = nombre
        self.profesores = profesores

    def obtener_profesores(self):
        # Método para obtener la lista de profesores de la materia
        return self.profesores

    def cambiar_nombre(self, nombre):
        # Método para cambiar el nombre de la materia
        self.nombre = nombre

    # Método para obtener la lista de alumnos de la materia
    def obtener_alumnos(self):
        return self.alumnos

# Definimos la clase Profesor
class Profesor:
    def __init__(self, nombre, cargo, legajo):
        # Inicializamos los atributos nombre, cargo y legajo del profesor
        self.nombre = nombre
        self.cargo = cargo
        self.legajo = legajo

    def obtener_nombre(self):
        # Método para obtener el nombre del profesor
        return self.nombre

    def obtener_cargo(self):
        # Método para obtener el cargo del profesor
        return self.cargo

    def obtener_legajo(self):
        # Método para obtener el legajo del profesor
        return self.legajo

# Definimos la clase que contendrá los tests para la clase Materia
class TestMateria(unittest.TestCase):
    # Test para comprobar el funcionamiento del constructor de Materia
    def test_constructor(self):
        nombre = "Matemáticas"
        profesores = ["Profesor1", "Profesor2"]
        # Creamos una instancia de Materia con valores específicos
        materia = Materia(nombre, profesores)
        # Comprobamos que los atributos se inicialicen correctamente
        self.assertEqual(materia.nombre, nombre)
        self.assertEqual(materia.profesores, profesores)

    # Test para comprobar el método cambiar_nombre de Materia
    def test_cambiar_nombre(self):
        materia = Materia("Historia", ["Profesor3"])
        nuevo_nombre = "Geografía"
        # Cambiamos el nombre de la materia
        materia.cambiar_nombre(nuevo_nombre)
        # Comprobamos que el nombre haya sido cambiado correctamente
        self.assertEqual(materia.nombre, nuevo_nombre)

    # Test para comprobar el método obtener_profesores de Materia
    def test_obtener_profesores(self):
        profesores = ["Profesor4", "Profesor5"]
        materia = Materia("Biología", profesores)
        # Comprobamos que se obtengan los profesores correctamente
        self.assertEqual(materia.obtener_profesores(), profesores)

# Definimos la clase que contendrá los tests para la clase Profesor
class TestProfesor(unittest.TestCase):
    # Test para comprobar el funcionamiento del constructor de Profesor
    def test_constructor(self):
        nombre = "Juan Pérez"
        cargo = "Profesor de Historia"
        legajo = 12345
        # Creamos una instancia de Profesor con valores específicos
        profesor = Profesor(nombre, cargo, legajo)
        # Comprobamos que los atributos se inicialicen correctamente
        self.assertEqual(profesor.nombre, nombre)
        self.assertEqual(profesor.cargo, cargo)
        self.assertEqual(profesor.legajo, legajo)

    # Test para comprobar el método obtener_nombre de Profesor
    def test_obtener_nombre(self):
        profesor = Profesor("Ana López", "Profesor de Matemáticas", 54321)
        # Comprobamos que se obtenga el nombre correctamente
        self.assertEqual(profesor.obtener_nombre(), "Ana López")

    # Test para comprobar el método obtener_cargo de Profesor
    def test_obtener_cargo(self):
        profesor = Profesor("Roberto García", "Profesor de Física", 98765)
        # Comprobamos que se obtenga el cargo correctamente
        self.assertEqual(profesor.obtener_cargo(), "Profesor de Física")

    # Test para comprobar el método obtener_legajo de Profesor
    def test_obtener_legajo(self):
        profesor = Profesor("María Martínez", "Profesor de Química", 13579)
        # Comprobamos que se obtenga el legajo correctamente
        self.assertEqual(profesor.obtener_legajo(), 13579)

# Ejecutamos los tests si este archivo es ejecutado directamente - Albarracin Gonzalo Nahuel
if __name__ == '__main__':
    unittest.main()

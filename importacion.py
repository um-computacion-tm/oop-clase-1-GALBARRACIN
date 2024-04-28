# importacion de las personas aca

from persona import Persona, crear_persona_mostrar_datos

# Creación de una instancia de la clase Persona con valores predeterminados y mostrando sus datos
persona_default = Persona()
persona_default.mostrar_datos()

# Creación de una instancia de la clase Persona con valores específicos y mostrando sus datos
persona_juan = Persona("Juan", "Perez", 987654)
persona_juan.mostrar_datos()

# Creación de una instancia de la clase Persona con un solo parámetro y mostrando sus datos
persona_maria = Persona(nombre="Maria")
persona_maria.mostrar_datos()

# Llamada a la función para crear una persona y mostrar sus datos - Albarracin Gonzalo Nahuel
crear_persona_mostrar_datos("Carlos", "Gonzalez", 654321)
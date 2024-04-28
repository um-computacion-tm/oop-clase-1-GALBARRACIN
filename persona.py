#Con correciones 
# persona.py

class Persona:
    def __init__(self, nombre: str = "john", apellido: str = "doe", du: int = 123456):
        # Inicialización de la clase Persona con atributos nombre, apellido y du (documento)
        self.__nombre__ = nombre  # Establece el nombre de la persona
        self.__apellido__ = apellido  # Establece el apellido de la persona
        self.__du__ = du  # Establece el número de documento de la persona

    def mostrar_datos(self):
        # Método para mostrar los datos de la persona
        print(
            f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__du__}'
        )

# Función para crear una instancia de la clase Persona con valores específicos y mostrar sus datos - Albarracin Gonzalo Nahuel
def crear_persona_mostrar_datos(nombre, apellido, du):
    persona = Persona(nombre, apellido, du)
    persona.mostrar_datos() 

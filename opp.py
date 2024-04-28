#Correciones 
class Profesor:
    def __init__(self, el_nombre, el_email):
        # Inicialización de la clase Profesor con nombre y email
        self.__nombre__ = el_nombre  # Establece el nombre del profesor
        self.__email__ = el_email  # Establece el email del profesor

    def dame_tu_nombre(self):
        # Método para obtener el nombre del profesor
        return self.__nombre__


class Alumno:
    def __init__(self, el_nombre_del_alumno):
        # Inicialización de la clase Alumno con nombre, inasistencias, dieta y mentor
        self.__nombre__ = el_nombre_del_alumno  # Establece el nombre del alumno
        self.__inasistencias__ = 0  # Inicializa el contador de inasistencias en 0
        self.__dieta__ = ""  # Inicializa la dieta como vacía
        self.__mentor__ = None  # Inicializa el mentor como None (ninguno)

    def mentoria(self, profesor):
        # Método para establecer el profesor mentor del alumno
        self.__mentor__ = profesor

    def falta(self):
        # Método para registrar una falta del alumno
        self.__inasistencias__ += 1

    def elegir_dieta_especial(self, la_dieta):
        # Método para elegir una dieta especial para el alumno
        self.__dieta__ = la_dieta

    def es_vegano(self):
        # Método para establecer que el alumno es vegano
        self.__dieta__ = "vegano"

    def esta_libre(self):
        # Método para verificar si el alumno está libre (más de 5 inasistencias)
        if self.__inasistencias__ >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"


# Creación de instancias de la clase Profesor
profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

# Creación de instancias de la clase Alumno
alumno_juan = Alumno("Juancito")
alumno_Maria = Alumno("Maria")

# Simulación de inasistencias para el alumno Juan
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())  # Imprime el estado de asistencia de Juan
alumno_juan.falta()
print(alumno_juan.esta_libre())  # Imprime el estado de asistencia de Juan nuevamente

# Establecimiento de dieta especial para el alumno María
alumno_Maria.elegir_dieta_especial("vegetariana")
print(alumno_Maria.__dieta__)  # Imprime la dieta especial de María
alumno_juan.es_vegano()  # Establece que Juan es vegano
print(alumno_juan.__dieta__)  # Imprime la dieta especial de Juan

# Establecimiento de mentoría para el alumno Juan con el profesor Elio
alumno_juan.mentoria(profe_elio)

print(alumno_juan.__mentor__)  # Imprime el mentor de Juan

# Línea para activar el depurador ipdb - Albarracin Gonzalo Nahuel
import ipdb; ipdb.set_trace()
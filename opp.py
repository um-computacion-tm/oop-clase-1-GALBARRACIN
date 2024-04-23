#Clases

class Profesor:
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email

    def dame_tu_nombre(self):
        return self.__nombre__

class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def falta(self):
        self.__inasistencias__ += 1

    def esta_libre(self):
        if self.__inasistencias__ > 5:
            return "Esta libre"
        else:
            return "Ok"
        
    def elegir_dieta_especial(self, dieta):
        self.__dieta__ = dieta

    def es_vegano(self):
        self.__dieta__ = "Vegano"

    def mentoria(self, profesor):
        self.__mentor__ = profesor


# Objetos y metodos

profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

profe_elio.dame_tu_nombre()
profe_gabi.dame_tu_nombre()

alumno_roman = Alumno("Roman")
alumno_juan = Alumno("Juancito")

print(profe_elio.__nombre__)
print(profe_gabi.__email__)

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())


alumno_juan.elegir_dieta_especial("Celiaco")
alumno_roman.es_vegano()

print(alumno_juan.__dieta__)
print(alumno_roman.__dieta__)

alumno_juan.mentoria(profe_elio)
alumno_roman.mentoria(profe_gabi)

print(alumno_juan.__mentor__)
print(alumno_roman.__mentor__.__nombre__)